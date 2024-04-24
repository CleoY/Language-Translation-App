// Define your API key
const apiKey = 'YOUR_API_KEY';

function sendRequest(message) {
    return fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: 'gpt-3.5-turbo',
            messages: [
                {
                    role: 'user',
                    content: message
                }
            ]
        })
    })
    .then(response => response.json())
    .catch(error => console.error('Error:', error));
}
