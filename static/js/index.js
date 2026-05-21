let button = document.getElementById("copy-btn");

button.addEventListener("click", function() {

    let text = document.getElementById("quote").innerText;

    navigator.clipboard.writeText(text);

    alert("Copied!");

});