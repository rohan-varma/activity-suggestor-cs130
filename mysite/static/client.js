// ----------------------------------------------------------------
// Generic web methods
// ----------------------------------------------------------------

/**
 * Builds query string from dictionary ("struct") fields.
 * @param {object} params - object containing query parameters as key-value pairs
 * @return {string} generated query string
 * @see https://stackoverflow.com/questions/111529/how-to-create-query-parameters-in-javascript
 */
function encodeQueryData(params) {
  let ret = [];
  for (let d in params)
    ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(params[d]));
  return ret.join('&');
}

/**
 * Builds an object from query string
 * @param {string} search - query string
 * @return {object} object with fields generated from the key-value pairs of the query string
 * @see https://stackoverflow.com/questions/8648892/convert-url-parameters-to-a-javascript-object
 */
function decodeQueryData(search) {
  search?JSON.parse('{"' + search.replace(/&/g, '","').replace(/=/g,'":"') + '"}',
    function(key, value) { return key===""?value:decodeURIComponent(value) }):{}
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
}

/**
 * Extracts the query string portion of the URL. Assumes that the query string exists, otherwise returns null
 * @return {string}
 */
function getUrlQueryString() {
  var u = window.location.href.split( '?' );
  if (u.length != 2) return null;
  else return u[1];
}


// ----------------------------------------------------------------
// Application methods
// ----------------------------------------------------------------

/**
 * Structure that stores geographical coordinates
 * @class LatLng
 * @property {number} lat
 * @property {number} lng
 */
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


// ----------------------------------------------------------------
// UI/Frontend methods
// ----------------------------------------------------------------

/**
 * Generates request URL for the recommender backend
 * @param {Object} params - object containing query parameters (as key-value pairs) that describe search parameters (current location, preferences, etc.)
 * @return {string} request URL for the recommender backend
 */
function getRecommenderUrl(params) {
  return url = getUrlRootPath() + "api/suggest/?" + encodeQueryData(params);
}

function getResultsPageUrl(params) {
  //return url = getUrlRootPath() + 
}

/**
 * 
 * Uses document state
 */
function loadUserInput() {
  if (document.getElementById("locationInput").value == "") {
    alert("Please enter your location!");
    //TODO| use something less intrusive
    return;
  }

  var params = {};
  params["location"] = document.getElementById("locationInput").value;
  params["radius"] = document.getElementById("distanceSelect").value;

  window.location.href = getRecommenderUrl(params); // for testing only
  //TODO
}

/**
 * 
 */
function requestSuggestionResults() {
  var req = new XMLHttpRequest();
  req.onreadystatechange = onSuggestionResultsLoad.bind(null, req);
  //req.responseText = "json"; // Me: "JSON! Yay! (Five minutes later) aw crap. No support in Internet Explorer or Edge."
  req.open("GET", getRecommenderUrl(suggestionPreferences));
  req.send();
}

function onSuggestionResultsLoad(req) {
  if (req.readyState == XMLHttpRequest.DONE && xhr.status === 200) {
    var json_response = JSON.parse(req.responseText);
  }
  //TODO| handle errors
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
  this.directionsService.route(
    {
      origin: new google.maps.LatLng(startLocation.lat, startLocation.lng),
      destination: new google.maps.LatLng(destLocation.lat, destLocation.lng),
      travelMode: travelMode
    }, 
    function(response, status) 
    {
      if (status === 'OK') {
        this.directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    }
  );
}

