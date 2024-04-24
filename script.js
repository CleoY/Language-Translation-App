document.addEventListener("DOMContentLoaded", function() {
    const generateButton = document.getElementById("generate-button");
    const inputText = document.getElementById("input-text");
    const outputText = document.getElementById("output-text");
    const responseSection = document.getElementById("response-section");

    generateButton.addEventListener("click", function() {
        const prompt = inputText.value.trim();
        if (prompt === "") {
            alert("Please enter a prompt.");
            return;
        }

        generateButton.disabled = true;
        responseSection.style.display = "none";

        // Set up the API endpoint
        const endpoint = 'https://api.openai.com/v1/engines/davinci/completions';

        // Set up the request data
        const requestData = {
            prompt: prompt,
            max_tokens: 100
        };

        // Set up the request headers
        const headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_OPENAI_API_KEY'
        };

        // Make the request
        fetch(endpoint, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            outputText.textContent = data.choices[0].text.trim();
            responseSection.style.display = "block";
        })
        .catch(error => {
            alert('Error:', error);
        })
        .finally(() => {
            generateButton.disabled = false;
        });
    });
});
