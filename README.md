# MamaCare 🤰🌸

MamaCare is an AI-powered pregnancy assistant that provides personalized health tips, reminders, and emotional support for expecting mothers. It uses multiple intelligent agents to answer questions, offer daily advice, and boost your mood.

---

## Features

- **Pregnancy Q&A:** Get medically-informed answers to your pregnancy questions.
- **Health Tips:** Receive nutrition and exercise tips tailored to your trimester and diet.
- **Reminders:** Stay on track with daily reminders for vitamins, hydration, and more.
- **Mood Support:** Enjoy gentle, encouraging messages based on your mood.

---

## Project Structure

```
mamacare/
│   .env
│   api.py
│   graph.py
│   main.py
│   requirements.txt
│   scheduler.py
│
├── agents/
│     __init__.py
│     health_agent.py
│     mood_agent.py
│     qa_agent.py
│     reminder_agent.py
│
├── frontend/
│     app.js
│     index.html
│     style.css
│
└── templates/
      response_template.md
```

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/mamacare.git
cd mamacare
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the `mamacare/` directory with your Google Gemini API key:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4. Run the backend API

From the parent directory of `mamacare/`, start the FastAPI server:

```sh
uvicorn mamacare.api:app --reload --port 8000
```

### 5. Run the frontend

Open `frontend/index.html` in your browser.  
The frontend will connect to the backend at `http://localhost:8000/ask`.

---

## Usage

- Ask pregnancy-related questions, select your trimester, diet, and mood.
- Get structured answers, daily tips, reminders, and mood support.

---

## Command-Line Interface

You can also run the assistant in the terminal:

```sh
python mamacare/main.py
```

---

## Scheduled Daily Tips

To receive daily tips at 9:00 AM, run:

```sh
python mamacare/scheduler.py
```

---

## Technologies Used

- Python, FastAPI
- LangGraph, LangChain, Google Generative AI
- JavaScript, HTML, CSS (Frontend)
- APScheduler

---

## License

MIT License

---

## Disclaimer

MamaCare is for informational purposes only and does not replace professional medical advice. Always consult your healthcare provider.

---

## Author

[Amaresh 🔥](https://github.com/yourusername)
