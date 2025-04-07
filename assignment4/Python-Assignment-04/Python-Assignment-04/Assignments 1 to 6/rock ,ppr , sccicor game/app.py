import streamlit as st
import random

# Initialize session state variables
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = "Let's Play!"
    st.session_state.user_choice = None
    st.session_state.computer_choice = None

# Title
st.title("✊✋✌ Rock, Paper, Scissors Game")

# Choices
choices = ["Rock ✊", "Paper ✋", "Scissors ✌"]

st.subheader("🎮 Choose your move:")

# Buttons for user choice
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✊ Rock"):
        st.session_state.user_choice = "Rock"
with col2:
    if st.button("✋ Paper"):
        st.session_state.user_choice = "Paper"
with col3:
    if st.button("✌ Scissors"):
        st.session_state.user_choice = "Scissors"

# If user made a choice
if st.session_state.user_choice:
    # Computer makes a random choice
    st.session_state.computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    # Game logic
    if st.session_state.user_choice == st.session_state.computer_choice:
        st.session_state.result = "🤝 It's a tie!"
    elif (st.session_state.user_choice == "Rock" and st.session_state.computer_choice == "Scissors") or \
         (st.session_state.user_choice == "Paper" and st.session_state.computer_choice == "Rock") or \
         (st.session_state.user_choice == "Scissors" and st.session_state.computer_choice == "Paper"):
        st.session_state.result = "🎉 You Win!"
        st.session_state.user_score += 1
    else:
        st.session_state.result = "😢 You Lose!"
        st.session_state.computer_score += 1

# Display Results
st.subheader(f"🧑 You: **{st.session_state.user_choice}**  VS  🤖 Computer: **{st.session_state.computer_choice}**")
st.markdown(f"## {st.session_state.result}")

# Scoreboard
st.subheader("🏆 Scoreboard")
st.write(f"**🧑 You:** {st.session_state.user_score}  |  **🤖 Computer:** {st.session_state.computer_score}")

# Reset Button
if st.button("🔄 Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = "Let's Play!"
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.rerun()

# Styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff5733;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)
