from graph import app

if __name__ == "__main__":
    print("Welcome to MamaCare 👶🌸")
    question = input("Ask a pregnancy-related question: ")
    trimester = input("Which trimester are you in? (1st/2nd/3rd): ")
    diet = input("Your diet? (veg/non-veg): ")
    mood = input("How are you feeling today? (happy/sad/anxious): ")

    result = app.invoke({
        "user_input": question,
        "trimester": trimester,
        "diet": diet,
        "mood": mood
    })
 
    print("\n🤖 Answer:", result["qa_answer"])
    print("🩺 Health Tips:\n", result["daily_tip"])
    print("🔔 Reminders:", "\n".join(result["reminders"]))
    print("💖 Mood Boost:", result["mood_response"])

    structured_result = {
    "qa_answer": result.get("qa_answer", ""),
    "daily_tip": result.get("daily_tip", ""),
    "reminders": result.get("reminders", []),
    "mood_response": result.get("mood_response", "")
}     
