chrome.runtime.onMessage.addListener(function(request, sender) {
  var message = document.getElementById('demo');

  if (request.action == "getSource") {
    message.innerHTML = ("Calling");
    /*if(true) {
      show("jQuery found");
    } else {
      show("No jQuery");
    }*/
  }
});

function onWindowLoad() {

  message = document.getElementById('demo');

  chrome.tabs.executeScript(null, {
    file: "jquery.js"
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

