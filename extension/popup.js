//var gm = require("gmail-js");

document.addEventListener('DOMContentLoaded', function() {
  //alert("loaded");
  //if(gm) { alert("gm not null"); }
  var checkPageButton = document.getElementById('checkPage');
  checkPageButton.addEventListener('click', function() {
    // document.getElementById("demo").innerHTML = "Hello World";
    //var gmail = gm.Gmail();
    //gmail.get.user_email();
//    document.getElementById("demo").innerHTML = "foo_bar";
  });
});

chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getSource") {
    document.getElementById("demo").innerHTML = request.source;
  }
});

function onWindowLoad() {

  var message = document.querySelector('#demo');

  chrome.tabs.executeScript(null, {
    file: "jquery.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });

  chrome.tabs.executeScript(null, {
    file: "gmail.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });


  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });

}

window.onload = onWindowLoad;
