# import time
# import random
# import colorama
# from colorama import Fore, Style

# # Initialize colorama
# colorama.init(autoreset=True)

# def get_input(prompt):
#     """Gets input from the user and ensures it's not empty."""
#     while True:
#         user_input = input(Fore.CYAN + prompt + Fore.RESET).strip()
#         if user_input:
#             return user_input
#         print(Fore.RED + "Oops! Please enter a valid response.\n")

# def mad_libs():
#     print(Fore.YELLOW + "\n🎉 Welcome to the Mad Libs Game! 🎉")
#     time.sleep(1)

#     # Getting user inputs
#     noun = get_input("Enter a noun: ")
#     verb = get_input("Enter a verb: ")
#     adjective = get_input("Enter an adjective: ")
#     place = get_input("Enter a place: ")

#     # List of random story templates
#     stories = [
#         f"\nOnce upon a time, in a {adjective} {place}, a {noun} was seen {verb}ing all around.\n"
#         "People were amazed and couldn't believe their eyes!",

#         f"\nThe {adjective} {noun} decided to {verb} in the middle of {place}.\n"
#         "Everyone gathered to watch, and it became the most memorable day ever!",

#         f"\nDeep in the heart of {place}, a {adjective} {noun} was on a mission.\n"
#         "Its goal? To {verb} its way to victory, and nothing could stop it!"
#     ]

#     # Select a random story
#     story = random.choice(stories)

#     # Display the final story with formatting
#     print(Fore.GREEN + "\n🎭 Here's your Mad Libs story! 🎭")
#     print(Fore.MAGENTA + "-" * 50)
#     print(Fore.BLUE + story)
#     print(Fore.MAGENTA + "-" * 50)

# def main():
#     """Runs the game with a replay option."""
#     while True:
#         mad_libs()
#         replay = input(Fore.YELLOW + "\nWould you like to play again? (yes/no): ").strip().lower()
#         if replay not in ["yes", "y"]:
#             print(Fore.RED + "\nThanks for playing! See you next time! 😊")
#             break

# # Run the game
# if __name__ == "__main__":
#     main()



import streamlit as st
import random

# Function to generate a Mad Libs story
def generate_story(noun, verb, adjective, place):
    stories = [
        f"Once upon a time, in a {adjective} {place}, a {noun} was seen {verb}ing all around.\n"
        "People were amazed and couldn't believe their eyes!",

        f"The {adjective} {noun} decided to {verb} in the middle of {place}.\n"
        "Everyone gathered to watch, and it became the most memorable day ever!",

        f"Deep in the heart of {place}, a {adjective} {noun} was on a mission.\n"
        "Its goal? To {verb} its way to victory, and nothing could stop it!"
    ]
    return random.choice(stories)

# Streamlit App UI
st.title("🎭 Mad Libs Game with Streamlit 🎭")
st.write("Fill in the blanks and create a funny story!")

# User Inputs
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")

# Generate Story Button
if st.button("Generate Story"):
    if noun and verb and adjective and place:
        story = generate_story(noun, verb, adjective, place)
        st.subheader("🎉 Your Mad Libs Story 🎉")
        st.success(story)
    else:
        st.error("⚠️ Please fill in all fields before generating a story.")

# Add some styling
st.markdown("""
<style>
    .stButton button {
        background-color: #ff5733;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)
