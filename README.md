# MamaCare 🤰 – Streamlit Frontend

This is a Streamlit-based web frontend for the MamaCare pregnancy assistant. It connects to the agent pipeline defined in [`main.py`](mamacare/main.py) and [`graph.py`](mamacare/graph.py), providing a user-friendly interface for expecting mothers to get personalized pregnancy advice, health tips, reminders, and mood support.

---

## Features

- **Ask Pregnancy Questions:** Get medically-informed answers.
- **Personalized Health Tips:** Nutrition and exercise tips based on your trimester and diet.
- **Reminders:** Stay on track with daily reminders.
- **Mood Support:** Receive gentle, encouraging messages based on your mood.

---

## Getting Started

### 1. Install Requirements

Make sure you have Python 3.8+ and install dependencies:

```sh
pip install streamlit python-dotenv google-generativeai langgraph langchain-core langchain-google-genai
```

### 2. Set Up Environment Variables

Create a `.env` file in the `mamacare/` directory with your Google Gemini API key:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

> **Note:** The `.env` file should be in the same directory as `streamlit_app.py`.

### 3. Run the Streamlit App

From the root of your project, run:

```sh
streamlit run mamacare/streamlit_app.py
```

This will open the MamaCare web app in your browser.

---

## Usage

1. Enter your pregnancy question.
2. Select your trimester, diet, and mood.
3. Click **Get Answer** to receive personalized advice, tips, reminders, and mood support.

---

## Project Structure

```
mamacare/
│   .env
│   streamlit_app.py
│   main.py
│   graph.py
│   scheduler.py
│   app.py
│
├── agents/
│     health_agent.py
│     mood_agent.py
│     qa_agent.py
│     reminder_agent.py
```

---

## Notes

- The Streamlit frontend uses the same agent pipeline as the CLI in [`main.py`](mamacare/main.py).
- For best results, ensure your `.env` file contains a valid Gemini API key.

---

## License

MIT License

---

## Disclaimer

MamaCare is for informational purposes only and does not replace professional medical advice. Always consult your healthcare provider.
