// Wait for the HTML to be fully loaded before running JS
document.addEventListener("DOMContentLoaded", () => {
    const urlBtn = document.getElementById("url-btn");
    const urlInput = document.getElementById("url-input");

    urlBtn.addEventListener("click", async (event) => {
        // Prevent any default browser behavior (e.g. form submission)
        event.preventDefault();


        const urlValue = urlInput.value.trim();
        if (!urlValue) {
            alert("Please enter a URL");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:5000/shorten/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url: urlValue })
            });
        
            const data = await response.json();
            // when you click shorten an input appears
            const resultContainer = document.getElementById("result-container");
            const shortUrlInput = document.getElementById("short-url");
            const copyBtn = document.getElementById("copy-btn");

            resultContainer.style.display = "flex";
            
            shortUrlInput.value = `http://127.0.0.1:5000/${data.short_code}`;

            copyBtn.addEventListener("click", () => {
                navigator.clipboard.writeText(shortUrlInput.value);

                copyBtn.textContent = "Copied!";

                setTimeout(() => {
                    copyBtn.textContent = "Copy";
                }, 1500);
            });
        } catch (error) {
            console.error(error);
        }
        
    });
});
