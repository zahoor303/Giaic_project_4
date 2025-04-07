import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="📊", layout="centered")

# Custom CSS for Dark Mode
dark_mode = st.sidebar.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
            body {background-color: #1E1E1E; color: white;}
            .stNumberInput>div>input {background-color: #333333; color: white;}
            .stButton>button {background-color: #444444; color: white;}
        </style>
        """, unsafe_allow_html=True
    )

# Title and description
st.title("💪 Body Mass Index (BMI) Calculator")
st.write("Enter your weight and height to calculate your BMI and see your health category.")

# Sidebar for input
st.sidebar.header("📌 Enter Your Details")
weight = st.sidebar.number_input("⚖️ Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
height = st.sidebar.number_input("📏 Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
    return round(weight / (height_m ** 2), 2)

# Function to calculate ideal weight range
def ideal_weight_range(height):
    height_m = height / 100
    lower = round(18.5 * (height_m ** 2), 1)
    upper = round(24.9 * (height_m ** 2), 1)
    return lower, upper

# Calculate BMI
if height and weight:
    bmi = calculate_bmi(weight, height)
    
    # Display result
    st.subheader(f"📊 Your BMI: **{bmi}**")

    # Ideal weight range
    ideal_lower, ideal_upper = ideal_weight_range(height)
    st.info(f"✅ Ideal Weight Range: **{ideal_lower} - {ideal_upper} kg**")

    # BMI categories & health tips
    if bmi < 18.5:
        st.warning("⚠️ **Underweight** - You may need to gain some weight.")
        st.write("💡 **Tip:** Eat a balanced diet with high-protein foods.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ **Normal weight** - Keep up the good work!")
        st.write("💡 **Tip:** Maintain a healthy lifestyle with exercise & balanced meals.")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ **Overweight** - Consider healthy weight management.")
        st.write("💡 **Tip:** Regular exercise & portion control can help.")
    else:
        st.error("⚠️ **Obese** - Consult a healthcare provider for guidance.")
        st.write("💡 **Tip:** Focus on healthy eating and physical activity.")

    # Progress Bar Visualization
    st.progress(min(bmi / 40, 1))  # Scale BMI to fit the bar

# Footer
st.markdown("---")
st.caption("🔹 Developed by ❤️ Zahoor fatima ")
