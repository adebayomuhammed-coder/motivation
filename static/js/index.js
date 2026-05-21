const copyBtn = document.getElementById("copy-btn");

copyBtn.addEventListener("click", () => {
    const text = document.getElementById("quote").innerText;

    navigator.clipboard.writeText(text).then(() => {

        // change text
        copyBtn.innerText = "Copied ✓";
        copyBtn.style.background = "#16a34a";

        // reset after 2 seconds
        setTimeout(() => {
            copyBtn.innerText = "Copy";
            copyBtn.style.background = "#1f2937";
        }, 2000);

    });
});