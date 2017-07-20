function loadLibraries() {
  /*var jq = document.createElement('script');
  jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js";
  document.getElementsByTagName('body')[0].appendChild(jq);*/

/*  var gm = document.createElement('script');
  gm.src = "https://raw.githubusercontent.com/KartikTalwar/gmail.js/master/src/gmail.js";
  document.getElementsByTagName('body')[0].appendChild(gm); */
}

function main() {
  //loadLibraries();

  //var gmail = Gmail();
  //return gmail.get.user_email();

  console.log("Extension loading...");
  gmail = new Gmail($);
  window.gmail = gmail;

gmail.observe.on("load", function() {
    userEmail = gmail.get.user_email();
    console.log("Hello, " + userEmail + ". This is your extension talking!");
});
}

chrome.runtime.sendMessage({
    action: "getSource",
    source: main()
});
