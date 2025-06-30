import streamlit as st
from graph import app

st.set_page_config(
    page_title="MamaCare - Pregnancy Assistant",
    page_icon="🤰",
    layout="centered"
)

st.title("🤰 MamaCare - Your Pregnancy Assistant")

with st.form("question_form"):
    question = st.text_area("Ask a pregnancy-related question:", height=100)
    trimester = st.selectbox("Which trimester are you in?", ["1st", "2nd", "3rd"])
    diet = st.radio("Your diet?", ["veg", "non-veg"])
    mood = st.select_slider(
        "How are you feeling today?",
        options=["sad", "anxious", "neutral", "good", "happy"],
        value="happy"
    )
    submitted = st.form_submit_button("Get Answer")

if submitted:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            result = app.invoke({
                "user_input": question,
                "trimester": trimester,
                "diet": diet,
                "mood": mood
            })
        st.success("Here's your personalized response:")
        st.markdown(f"**🤖 Answer:** {result.get('qa_answer', '')}")
        st.markdown(f"**🩺 Health Tips:** {result.get('daily_tip', '')}")
        reminders = result.get("reminders", [])
        if reminders:
            st.markdown("**🔔 Reminders:**")
            for r in reminders:
                st.markdown(f"- {r}")
        st.markdown(f"**💖 Mood Boost:** {result.get('mood_response', '')}")