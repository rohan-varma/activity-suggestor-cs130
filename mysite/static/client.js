// ----------------------------------------------------------------
// Generic web methods
// ----------------------------------------------------------------

/**
 * Builds query string from dictionary ("struct") fields.
 * @param {object} params - object containing query parameters as key-value pairs
 * @return {string} generated query string
 */
function encodeQueryData(params) {
  var result = [];
  for (let d in params)
    result.push(encodeURIComponent(d) + '=' + encodeURIComponent(params[d]));
  return result.join('&');
}

/**
 * Builds an object from query string
 * @param {string} search - query string
 * @return {object} object with fields generated from the key-value pairs of the query string
 */
function decodeQueryData(query) {
  var result = {};
  query.split('&').forEach(function(pair) {
      pair = pair.split('=');
      result[pair[0]] = decodeURIComponent(pair[1] || '');
  });
  return result;
}

/**
 * Extracts the scheme + domain parts of the URL
 * @return {string}
 */
function getUrlRootPath() {
  var pathArray = window.location.href.split( '/' );
  var protocol = pathArray[0];
  var host = pathArray[2];
  return protocol + '//' + host + "/";
  //*| the most idiomatic solution is to use Location.origin + "/"; however, some browsers don't support it
}

/**
 * Extracts the query string portion of the URL. Assumes that the query string exists, otherwise returns null
 * @return {string}
 */
function getUrlQueryString() {
  return window.location.search.slice(1);
}

/**
 * 
 */
function toggleBlockDisplay(element)
{
  var r;
  switch (window.getComputedStyle(element).display) {
    case "none": r = "block"; break;
    default: r = "none"; break;
  }
  element.style.display = r;
}


// ----------------------------------------------------------------
// Application methods
// ----------------------------------------------------------------

/**
 * Structure that stores geographical coordinates
 * @typedef {object} LatLng
 * @property {number} lat
 * @property {number} lng
 */

// TODO| theres no point in making this a constructed object right now (since it doesn't interop with Google's anyway)
function LatLng(lat, lng) {
  this.lat = lat;
  this.lng = lng;
}

/**
 * Extracts and validates latitude and longitude from string
 * @param {string} locstring - string describing latitude and longitude of a location, given in the format "lat,lng"
 * @return {LatLng} null if conversion failed
 */
function parseLatLng(locstring)
{
  if (locstring == null) // null or undefined
    return null;

  var arr = locstring.split(",");
  if (arr.length != 2)
    return null;
  var lat = parseFloat(arr[0]);
  var lng = parseFloat(arr[1]);
  // NaN if string is in bad format

  if (!(lat <= 90 && lat >= -90 && lng <= 180 && lng >= -180))
    return null;
  
  return new LatLng(lat, lng);
}

/**
 * 
 */
function printLatLng(latlng)
{
  if (latlng == null)
    return null;
  return latlng.lat.toString() + "," + latlng.lng.toString();
}

/**
 * An object that describes search parameters (current location, preferences, etc.)
 * @typedef {object} RecommenderParams
 * @property {string} location - the start location
 * @property {string} [distance] - the maximum distance, measured in meters; default is 8000
 * @property {string} [when] - //TODO> as of this moment, only "time of day" is supported
 * @property {string[]} [placeType] - //TODO
 */


// ----------------------------------------------------------------
// UI/Frontend methods
// ----------------------------------------------------------------

/**
 * Generates request URL for the recommender backend
 * @param {object} params
 * @return {string}
 */
function getRecommenderUrl(params) {
  return url = getUrlRootPath() + "api/suggest/?" + encodeQueryData(params);
}

/**
 * Generates URL for the results page
 * "window.location.href = getResultsPageUrl(getUserInput());"
 * @param {object} params
 * @return {string}
 */
function getResultsPageUrl(params) {
  return url = getUrlRootPath() + "main?" + encodeQueryData(params);
}


/**
 * Converts user entered data in the input fields to an object
 * Uses document state
 * @return {RecommenderParams} object that describes search parameters (current location, preferences, etc.)
 */
function getUserInput() {
  var params = {};
  params["location"] = document.getElementById("locationInput").value;
  params["distance"] = document.getElementById("distanceSelect").value;
  params["when"] = document.getElementById("hoursSelect").value;
  
  return params;
}

//TODO| validation/error-checking
/* function validateUserInput(interactive) {
  if (interactive === undefined) interactive = true; //default

  if (document.getElementById("locationInput").value == "") {
    if (interactive) alert("Please enter your location!");
    return;
  }
  //e.g. max distance supported by Google Places is 50 km. Let's worry about converting to miles later. Maybe validation should be a separate thing.
}*/

//TODO| also need a method to set the input controls from current parameters (for, say, redirecting from/to the results page)

//TODO| session storage when user clicks on "Show Map" in splash? (Rather than passing via query parameters)


/**
 * Retrieves place recommender suggestion results from backend
 * No parameters; uses globals
 */
function requestSuggestionResults() {
  var req = new XMLHttpRequest();
  req.onreadystatechange = onSuggestionResultsLoad.bind(null, req);
  req.open("GET", getRecommenderUrl(queryParams));
  //TODO| might need to clean up the param fields if other options are added in the future
  req.send();
}

/**
 * Processes place recommender suggestion results retrieved from backend.
 */
function onSuggestionResultsLoad(req) {
  if (req.readyState == XMLHttpRequest.DONE) {
    if (req.status === 200) {
      var j = JSON.parse(req.responseText);
      destLocationInfoArr = j.results;
      nextPageToken = j.next_page_token;

      if (destLocationInfoArr.length == 0)
      {
        //TODO| "no results found"
        ;
      }
      else
        showNext(); // from -1 to 0
      }
    }
    else {
      document.getElementById("???").innerHTML = "ERROR: failed to retrieve data\n(" + req.status + ")";
    }
  }
}

/**
 * Requests the next page of results
 * //TODO| this might not actually be the intended behavior
 */
function requestSuggestionResultsNextPage() {
  if (nextPageToken == null) {
    //TODO| show "no more results" warning
    return false;
  }
  var req = new XMLHttpRequest();
  req.onreadystatechange = onSuggestionResultsNextPageLoad.bind(null, req);
  req.open("GET", getRecommenderUrl({pagetoken: next_page_token}));
  req.send();
  return true;
}

function onSuggestionResultsNextPageLoad(req) {
  if (req.readyState == XMLHttpRequest.DONE) {
    var increment_count = 0;
    if (req.status === 200) {
      var j = JSON.parse(req.responseText);
      try {
        destLocationInfoArr = destLocationInfoArr.concat(j.results);
        nextPageToken = j.next_page_token;
        increment_count = j.results.length;
      }
      catch (e) {
        nextPageToken = null;
      }

      if (increment_count == 0)
      {
        //TODO| "something happened"
        ;
      }
      else
        showNext();
    }
    else {
      document.getElementById("???").innerHTML = "ERROR: failed to retrieve data\n(" + req.status + ")";
    }
  }
}

/**
 * Displays the next suggestion in the queue.
 */
function showNext() {
  if (destIndex + 1 == destLocationInfoArr.length)
  {
    requestSuggestionResultsNextPage();
  }
  else
  {
    destIndex = destIndex + 1;
    var curDestLocation = destLocationInfoArr[destIndex];
    mapService.getAndDisplayRoute(startLocation, curDestLocation.geometry.location, travelMode);

    document.getElementById('selLocName').textContent = curDestLocation.name;
    document.getElementById('selLocAddr').textContent = curDestLocation.formatted_address;
    document.getElementById('selLocLatLng').textContent = printLatLng(curDestLocation.geometry.location);
    document.getElementById('selLocHours').textContent =
      curDestLocation.permanently_closed ?
        "Permanently closed":
        ((curDestLocation.opening_hours && curDestLocation.opening_hours.open_now) ?
          "Open ???" :
          "Closed right now"
          //TODO
        );
  }
}

/**
 * 
 */
function acceptSuggestion() {
  //TODO
}


/**
 * Encapsulates the Google Maps API
 * @class MapService
 * @property {google.maps.DirectionsService} directionsService
 * @property {google.maps.DirectionsRenderer} directionsDisplay
 */
function MapService()
{
  this.directionsService = new google.maps.DirectionsService;
  this.directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: {lat: 41.85, lng: -87.65},
    zoomControl: true,
    mapTypeControl: true,
    streetViewControl: true
  });
  this.directionsDisplay.setMap(map);
}

/**
 * @function
 * @memberof MapService
 * @param {LatLng} startLocation
 * @param {LatLng} destLocation
 * @param {string} travelMode - DRIVING, ... etc. <TODO>
 */
MapService.prototype.getAndDisplayRoute = 
function (startLocation, destLocation, travelMode) 
{
  var self_capture = this;
  this.directionsService.route(
    {
      origin: new google.maps.LatLng(startLocation.lat, startLocation.lng),
      destination: new google.maps.LatLng(destLocation.lat, destLocation.lng),
      travelMode: travelMode
    }, 
    function(response, status) 
    {
      if (status === 'OK') {
        self_capture.directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    }
  );
}

/**
 * @see https://developers.google.com/maps/documentation/javascript/events#EventArguments
 */
function placeMarker(map, location) 
{
  var marker = new google.maps.Marker({
      position: location, 
      map: map
  });
  return marker;
}

/**
 * 
 */
function removeMarker(marker)
{
  marker.setMap(null);
}
