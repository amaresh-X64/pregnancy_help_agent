import streamlit as st
from graph import app
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="MamaCare - Your Pregnancy Assistant",
    page_icon="🤰",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {font-size: 2.5rem; color: #FF69B4; text-align: center; margin-bottom: 1rem;}
    .sub-header {font-size: 1.5rem; color: #FF69B4; margin-top: 1.5rem;}
    .stButton>button {background-color: #FF69B4; color: white; border: none; padding: 0.5rem 2rem; border-radius: 5px;}
    .stButton>button:hover {background-color: #FF1493;}
    .response-box {background-color: #FFF0F5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;}
    .reminder-item {margin: 0.5rem 0; padding-left: 1rem; border-left: 3px solid #FF69B4;}
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='main-header'>🤰 MamaCare - Your Pregnancy Assistant</h1>", unsafe_allow_html=True)

# Sidebar for user inputs
with st.sidebar:
    st.header("👤 Your Information")
    trimester = st.selectbox("Which trimester are you in?", ["1st", "2nd", "3rd"])
    diet = st.radio("Your diet:", ["Vegetarian", "Non-Vegetarian"])
    mood = st.select_slider(
        "How are you feeling today?",
        options=["😢 Sad", "😟 Anxious", "😐 Neutral", "🙂 Good", "😊 Happy"]
    )

# Main content
st.markdown("### 💬 Ask me anything about your pregnancy")
user_input = st.text_area("Type your question here...", height=100)

if st.button("Get Advice"):
    if not user_input.strip():
        st.warning("Please enter a question first!")
    else:
        with st.spinner("🤔 Thinking..."):
            # Prepare inputs for the agent
            inputs = {
                "user_input": user_input,
                "trimester": trimester,
                "diet": diet.lower(),
                "mood": mood.split()[-1].lower(),  # Extract the mood (happy/sad/etc.)
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Get response from the agent
            result = app.invoke(inputs)
            
            # Display the response
            st.markdown("<div class='response-box'>", unsafe_allow_html=True)
            
            st.markdown("### 💡 Answer")
            st.write(result.get("qa_answer", "No answer provided."))
            
            st.markdown("### 🩺 Health Tips")
            st.write(result.get("daily_tip", "No health tips available."))
            
            st.markdown("### 🔔 Reminders")
            reminders = result.get("reminders", [])
            if reminders:
                for reminder in reminders:
                    st.markdown(f"<div class='reminder-item'>{reminder}</div>", unsafe_allow_html=True)
            else:
                st.write("No reminders at the moment.")
            
            mood_response = result.get("mood_response", "")
            if mood_response:
                st.markdown("### 💖 Mood Boost")
                st.write(mood_response)
            
            st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; margin-top: 2rem;'>
        <p>🤰 MamaCare - Your trusted pregnancy companion</p>
        <p>Always consult with your healthcare provider for medical advice</p>
    </div>
""", unsafe_allow_html=True)
