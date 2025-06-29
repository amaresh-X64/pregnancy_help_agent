document.getElementById('mamacare-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const question = document.getElementById('question').value;
    const trimester = document.getElementById('trimester').value;
    const diet = document.getElementById('diet').value;
    const mood = document.getElementById('mood').value;

    const payload = {
        user_input: question,
        trimester: trimester,
        diet: diet,
        mood: mood
    };

    // Change the URL below to your backend endpoint
    const apiUrl = 'http://localhost:8000/ask'; // Example: FastAPI/Flask endpoint

    const resultsDiv = document.getElementById('results');
    resultsDiv.style.display = 'block';
    resultsDiv.innerHTML = '<em>Loading...</em>';

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await response.json();

        resultsDiv.innerHTML = `
            <h2>🤖 Answer</h2>
            <p>${data.qa_answer || ''}</p>
            <h2>🩺 Health Tips</h2>
            <p>${data.daily_tip || ''}</p>
            <h2>🔔 Reminders</h2>
            <ul>${(data.reminders || []).map(r => `<li>${r}</li>`).join('')}</ul>
            <h2>💖 Mood Boost</h2>
            <p>${data.mood_response || ''}</p>
        `;
    } catch (err) {
        resultsDiv.innerHTML = '<span style="color:red;">Error: Could not connect to backend.</span>';
    }
});