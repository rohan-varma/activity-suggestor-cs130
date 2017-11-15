/* function OnLoad() {

} */

function encodeQueryData(data) {
  let ret = [];
  for (let d in data)
    ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(data[d]));
  return ret.join('&');
}

function constructUrl(){
  var pathArray = location.href.split( '/' );
  var protocol = pathArray[0];
  var host = pathArray[2];
  var url = protocol + '//' + host + "/";
  url += "api/suggest/";

  if (document.getElementById("locationInput").value != "") {
    alert("Please enter your location!");
    //TODO
  }
  else {
    var params = {};
    params["location"] = document.getElementById("locationInput").value;
    params["radius"] = document.getElementById("distanceSelect").value;
    url += "?" + encodeQueryData(params);
    
    window.location.href = url; // for testing only
    //console.log(JSON.stringify(url, null, 2));

    //window.location.replace(url);
  }
}
// console.log(window.location.href);
