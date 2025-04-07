import streamlit as st
import random

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.difficulty = "Medium"  # Default difficulty
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# Difficulty Levels
difficulty_ranges = {
    "Easy": (1, 50),
    "Medium": (1, 100),
    "Hard": (1, 200)
}

# Streamlit App Title
st.title("🎯 Guess the Number Game!")
st.write("Try to guess the number based on the difficulty level you choose.")

# Select Difficulty Level
difficulty = st.selectbox("Select Difficulty:", ["Easy", "Medium", "Hard"], index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty))

# If difficulty changes, reset the game
if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret_number = random.randint(*difficulty_ranges[difficulty])
    st.session_state.attempts = 0

# Define range based on difficulty
min_val, max_val = difficulty_ranges[difficulty]

# User Input
guess = st.number_input(f"Enter your guess ({min_val} - {max_val}):", min_value=min_val, max_value=max_val, step=1)

# Submit Button
if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("🔼 Too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.warning("🔽 Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts!")
        st.session_state.secret_number = random.randint(*difficulty_ranges[difficulty])  # Reset for new game
        st.session_state.attempts = 0  # Reset attempts



# Styling the UI
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff5733;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    .stNumberInput>div>div>input {
        font-size: 16px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)
