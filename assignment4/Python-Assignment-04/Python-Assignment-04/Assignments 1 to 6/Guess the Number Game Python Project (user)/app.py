import streamlit as st
import random
import time

# Initialize session state variables
if "low" not in st.session_state:
    st.session_state.difficulty = "Medium"  # Default difficulty
    st.session_state.low, st.session_state.high = 1, 100  # Default range
    st.session_state.attempts = 0
    st.session_state.leaderboard = []
    st.session_state.game_active = True

# Define difficulty levels
difficulty_ranges = {
    "Easy": (1, 50),
    "Medium": (1, 100),
    "Hard": (1, 200)
}

# Streamlit App Title
st.title("🤖 Computer Guesses Your Number!")
st.write("Think of a number, and I'll guess it!")

# Difficulty Selection
difficulty = st.selectbox("Select Difficulty:", ["Easy", "Medium", "Hard"], index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty))

# If difficulty changes, reset the game
if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.low, st.session_state.high = difficulty_ranges[difficulty]
    st.session_state.attempts = 0
    st.session_state.game_active = True

# Generate computer's guess (only if game is active)
if st.session_state.game_active:
    if "computer_guess" not in st.session_state or st.session_state.low > st.session_state.high:
        st.session_state.low, st.session_state.high = difficulty_ranges[difficulty]
    
    st.session_state.computer_guess = (st.session_state.low + st.session_state.high) // 2

st.subheader(f"Is your number **{st.session_state.computer_guess}**?")

# Feedback Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔽 Too High"):
        if st.session_state.low < st.session_state.high:
            st.session_state.high = st.session_state.computer_guess - 1
            st.session_state.attempts += 1
            st.session_state.computer_guess = (st.session_state.low + st.session_state.high) // 2
            st.rerun()
        else:
            st.error("🤔 The range is incorrect. Click 'Play Again'.")

with col2:
    if st.button("✅ Correct!"):
        st.success(f"🎉 I guessed your number **{st.session_state.computer_guess}** in **{st.session_state.attempts}** attempts!")

        # Save best score
        if st.session_state.attempts > 0:
            st.session_state.leaderboard.append(st.session_state.attempts)
            st.session_state.leaderboard.sort()

        # Confetti effect 🎉
        time.sleep(1)
        st.balloons()

        st.session_state.game_active = False  # Stop the game

with col3:
    if st.button("🔼 Too Low"):
        if st.session_state.low < st.session_state.high:
            st.session_state.low = st.session_state.computer_guess + 1
            st.session_state.attempts += 1
            st.session_state.computer_guess = (st.session_state.low + st.session_state.high) // 2
            st.rerun()
        else:
            st.error("🤔 The range is incorrect. Click 'Play Again'.")

# Show Leaderboard
if st.session_state.leaderboard:
    st.subheader("🏆 Leaderboard - Best Scores")
    for idx, score in enumerate(st.session_state.leaderboard[:5], start=1):
        st.write(f"🥇 Attempt {idx}: {score} guesses")

# Play Again Button
if not st.session_state.game_active or st.button("🔄 Play Again"):
    st.session_state.low, st.session_state.high = difficulty_ranges[difficulty]
    st.session_state.attempts = 0
    st.session_state.game_active = True
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
