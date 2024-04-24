document.addEventListener("DOMContentLoaded", function() {
    const generateButton = document.getElementById("generate-button");
    const inputText = document.getElementById("input-text");
    const outputText = document.getElementById("output-text");
    const responseSection = document.getElementById("response-section");
    const navigationSection = document.getElementById("navigation-section");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");

    // Array to store prompts and responses
    let prompts = [];
    let responses = [];
    let currentIndex = 0;

    // Function to handle the "Generate" button click
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

            // Add prompt and response to the arrays
            prompts.push(prompt);
            responses.push(data.choices[0].text.trim());
            currentIndex = prompts.length - 1;
            updateNavigationButtons();
        })
        .catch(error => {
            alert('Error:', error);
        })
        .finally(() => {
            generateButton.disabled = false;
        });
    });

    // Function to handle the "Next" button click
    nextButton.addEventListener("click", function() {
        currentIndex++;
        displayResponse();
    });

    // Function to handle the "Previous" button click
    prevButton.addEventListener("click", function() {
        currentIndex--;
        displayResponse();
    });

    // Function to display the response based on the current index
    function displayResponse() {
        inputText.value = prompts[currentIndex];
        outputText.textContent = responses[currentIndex];
        updateNavigationButtons();
    }

    // Function to update navigation buttons based on the current index
    function updateNavigationButtons() {
        prevButton.disabled = currentIndex === 0;
        nextButton.disabled = currentIndex === prompts.length - 1;
        navigationSection.style.display = prompts.length > 1 ? "block" : "none";
    }
});
