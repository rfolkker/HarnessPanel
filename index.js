var csInterface = new CSInterface();
/* Make a reference to your HTML button and add a click handler. */
var openButton = document.querySelector("#open-button");
openButton.addEventListener("click", openDoc);
/* Write a helper function to pass instructions to the ExtendScript side. */
function openDoc() {
  csInterface.evalScript("openDocument()");
}

/* 2) Use a CEP method to open the server extension. */
csInterface.requestOpenExtension("com.dnv.localserver", "");