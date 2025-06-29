from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend JS to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    user_input: str
    trimester: str
    diet: str
    mood: str

@app.post("/ask")
async def ask_agent(query: Query):
    # Replace these with real agent calls
    return {
        "qa_answer": f"Answer to: {query.user_input}",
        "daily_tip": f"Tip for {query.trimester} trimester and {query.diet} diet.",
        "reminders": ["Take prenatal vitamins", "Drink water"],
        "mood_response": f"You're feeling {query.mood}. Stay positive!"
    }