function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    fetch('/api/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data.result);
    })
    .catch(error => console.error('Error:', error));
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = results;
}

function goToResults() {
    window.location.href = 'results.html'; // Navigate to the results page
}

function goToAbout() {
    window.location.href = 'about.html'; // Navigate to the about page
}

function goToHome() {
    window.location.href = 'index.html'; // Navigate to the home page
}
