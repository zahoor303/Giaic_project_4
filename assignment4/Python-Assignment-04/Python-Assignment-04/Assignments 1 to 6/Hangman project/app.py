# import streamlit as st
# import random

# # Word list for the game
# words = ["python", "streamlit", "developer", "hangman", "coding", "challenge", "programming"]

# # Initialize session state variables
# if "word" not in st.session_state:
#     st.session_state.word = random.choice(words)
#     st.session_state.guessed_letters = []
#     st.session_state.attempts_left = 6
#     st.session_state.game_over = False

# # Function to display the current guessed word state
# def get_display_word():
#     return " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])

# # Function to check the game state
# def check_game_state():
#     if "_" not in get_display_word():
#         st.session_state.game_over = True
#         return "🎉 You Win! The word was **" + st.session_state.word + "**"
#     elif st.session_state.attempts_left <= 0:
#         st.session_state.game_over = True
#         return "😢 You Lost! The word was **" + st.session_state.word + "**"
#     return None

# # UI
# st.title("🕵️ Hangman Game")
# st.subheader("Guess the word letter by letter!")

# st.write(f"Word to guess: **{get_display_word()}**")
# st.write(f"🔢 Attempts Left: **{st.session_state.attempts_left}**")

# # Alphabet buttons
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# cols = st.columns(9)

# for i, letter in enumerate(alphabet):
#     with cols[i % 9]:
#         if st.button(letter, key=letter, disabled=(letter in st.session_state.guessed_letters or st.session_state.game_over)):
#             st.session_state.guessed_letters.append(letter)
#             if letter not in st.session_state.word:
#                 st.session_state.attempts_left -= 1
#             st.rerun()

# # Check game result
# result_message = check_game_state()
# if result_message:
#     st.subheader(result_message)

# # Reset button
# if st.session_state.game_over or st.button("🔄 Play Again"):
#     st.session_state.word = random.choice(words)
#     st.session_state.guessed_letters = []
#     st.session_state.attempts_left = 6
#     st.session_state.game_over = False
#     st.rerun()

# # Styling
# st.markdown("""
# <style>
#     .stButton>button {
#         background-color: #3498db;
#         color: white;
#         font-size: 16px;
#         padding: 8px;
#         border-radius: 6px;
#         margin: 2px;
#     }
# </style>
# """, unsafe_allow_html=True)




import streamlit as st
import random

# Word list
words = ["python", "streamlit", "developer", "hangman", "coding", "challenge", "programming"]

# Hangman stages (ASCII art)
HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """  # Final stage (Game Over)
]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts_left = 6
    st.session_state.game_over = False
    st.session_state.hint_used = False

# Function to display the word progress
def get_display_word():
    return " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])

# Function to check game state
def check_game_state():
    if "_" not in get_display_word():
        st.session_state.game_over = True
        return "🎉 You Win! The word was **" + st.session_state.word + "**"
    elif st.session_state.attempts_left <= 0:
        st.session_state.game_over = True
        return "😢 You Lost! The word was **" + st.session_state.word + "**"
    return None

# UI
st.title("🕵️ Hangman Game")
st.subheader("Guess the word letter by letter!")

# Display Hangman ASCII Art based on mistakes
st.code(HANGMAN_PICS[6 - st.session_state.attempts_left], language="")

st.write(f"Word to guess: **{get_display_word()}**")
st.write(f"🔢 Attempts Left: **{st.session_state.attempts_left}**")

# Alphabet buttons
alphabet = "abcdefghijklmnopqrstuvwxyz"
cols = st.columns(9)

for i, letter in enumerate(alphabet):
    with cols[i % 9]:
        if st.button(letter, key=letter, disabled=(letter in st.session_state.guessed_letters or st.session_state.game_over)):
            st.session_state.guessed_letters.append(letter)
            if letter not in st.session_state.word:
                st.session_state.attempts_left -= 1
            st.rerun()

# Hint button (only once)
if not st.session_state.hint_used and st.button("🆘 Get a Hint"):
    for letter in st.session_state.word:
        if letter not in st.session_state.guessed_letters:
            st.session_state.guessed_letters.append(letter)
            st.session_state.hint_used = True
            break
    st.rerun()

# Check game result
result_message = check_game_state()
if result_message:
    st.subheader(result_message)

# Reset button
if st.session_state.game_over or st.button("🔄 Play Again"):
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts_left = 6
    st.session_state.game_over = False
    st.session_state.hint_used = False
    st.rerun()

# Styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-size: 16px;
        padding: 8px;
        border-radius: 6px;
        margin: 2px;
    }
</style>
""", unsafe_allow_html=True)
