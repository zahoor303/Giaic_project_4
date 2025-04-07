import streamlit as st
import time


# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
    st.session_state.time_left = 0
    st.session_state.end_time = None

# Function to start the countdown
def start_timer(hours, minutes, seconds):
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    if total_seconds > 0:
        st.session_state.running = True
        st.session_state.time_left = total_seconds
        st.session_state.end_time = time.time() + total_seconds
        st.rerun()  # ✅ FIXED: Use st.rerun() instead of st.experimental_rerun()

# Function to reset the timer
def reset_timer():
    st.session_state.running = False
    st.session_state.time_left = 0
    st.session_state.end_time = None
    st.rerun()

# Function to play an alarm sound

# UI Layout
st.title("⏳ Countdown Timer")

# User input for time
col1, col2, col3 = st.columns(3)
with col1:
    hours = st.number_input("Hours", min_value=0, max_value=23, value=0, step=1)
with col2:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0, step=1)
with col3:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=10, step=1)

# Start and Reset buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("▶ Start Timer"):
        start_timer(hours, minutes, seconds)
with col2:
    if st.button("⏹ Reset Timer"):
        reset_timer()

# Countdown logic (Live update)
if st.session_state.running:
    st.session_state.time_left = max(0, int(st.session_state.end_time - time.time()))

    if st.session_state.time_left > 0:
        mins, secs = divmod(st.session_state.time_left, 60)
        hrs, mins = divmod(mins, 60)
        st.subheader(f"⏳ {hrs:02d}:{mins:02d}:{secs:02d} Remaining")
        st.progress(1 - st.session_state.time_left / (int(hours) * 3600 + int(minutes) * 60 + int(seconds)))
        time.sleep(1)
        st.rerun()  # ✅ FIXED
    else:
        st.session_state.running = False
        st.success("⏰ Time's up!")
      
        st.balloons()
