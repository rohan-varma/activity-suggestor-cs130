// ----------------------------------------------------------------
// Generic methods
// ----------------------------------------------------------------

/**
 * Builds query string from dictionary ("struct") fields.
 * @param {object} params - struct of parameters
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
 * @return {object} - object with fields generated from the key-value pairs of the query string
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


// ----------------------------------------------------------------
// Application methods
// ----------------------------------------------------------------

/**
 * Validates parameters
 * TODO: do we actually need a separate func for this???
 */
function validateLocationRequestParams() {
  
}

/**
 * 
 */
function getRecommenderUrl(params) {
  var url = getUrlRootPath() + "api/suggest/" + encodeQueryData(params);

}
// console.log(window.location.href);

/**
 * 
 */
function loadResults_SplashPage() {
  if (document.getElementById("locationInput").value != "") {
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
function loadResults_ResultsPage() {

}
