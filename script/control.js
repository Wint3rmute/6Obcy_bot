document.getElementById("seekG").addEventListener("click", G);
document.getElementById("seekB").addEventListener("click", B);
document.getElementById("stop").addEventListener("click", S);
document.getElementById("author").addEventListener("click", author);
document.getElementById("manual").addEventListener("click", manual);

var seeking = false;

function manual()
{
  var newURL = "https://wint3rmute.github.io/6obcy/manual.html";
    chrome.tabs.create({ url: newURL });

}

function author()
{
  var newURL = "https://github.com/Wint3rmute";
    chrome.tabs.create({ url: newURL });
}

function B(){
  if(seeking!=true)
  sendToScript("seekBoys");
  seeking = true;
}


function G(){
  if(seeking!=true)
  sendToScript("seekGirls");
  seeking = true;
}


function S(){
  seeking = false;
  sendToScript("stop");
}

function sendToScript(messageContent)
{
  console.log("sending " + messageContent);

  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
chrome.tabs.sendMessage(tabs[0].id, {message: messageContent}, function(response) {});
});
}
