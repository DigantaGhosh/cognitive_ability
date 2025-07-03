# app.py

import streamlit as st
import qrcode
from PIL import Image

# -------------------------------
# Title and Description
# -------------------------------
st.set_page_config(page_title="Cognitive Ability Predictor", layout="centered")
st.title("🧠 Cognitive Ability Score Predictor")
st.markdown("""
This app predicts your **Cognitive Ability Score** using a regression model based on lifestyle and demographic inputs.
It also classifies the score as **High** or **Low**.
""")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Enter Your Information")

age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
memory_test_score = st.sidebar.slider("Memory Test Score (0-100)", 0.0, 100.0, 70.0)
stress_level = st.sidebar.slider("Stress Level (1-10)", 1.0, 10.0, 5.0)
diet_type = st.sidebar.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
reaction_time = st.sidebar.number_input("Reaction Time (seconds)", 0.1, 5.0, 0.5)
daily_screen_time = st.sidebar.slider("Daily Screen Time (hours)", 0.0, 16.0, 5.0)
caffeine_intake = st.sidebar.number_input("Caffeine Intake (cups/day)", 0.0, 10.0, 1.0)
exercise_freq = st.sidebar.selectbox("Exercise Frequency", ["None", "Low", "High"])

# -------------------------------
# Encode Inputs
# -------------------------------
gender_female = 1 if gender == "Female" else 0
diet_nonveg = 1 if diet_type == "Non-Vegetarian" else 0
diet_vegan = 1 if diet_type == "Vegan" else 0
exercise_high = 1 if exercise_freq == "High" else 0
exercise_low = 1 if exercise_freq == "Low" else 0

# -------------------------------
# Prediction using Linear Model
# -------------------------------
cognitive_score = (
    104.22095
    + 0.0002346 * age
    + 0.0053528 * gender_female
    + 1.9273209 * sleep_duration
    + 0.4847063 * memory_test_score
    - 1.930593 * stress_level
    - 0.017732 * diet_nonveg
    - 0.002951 * diet_vegan
    - 0.163666 * reaction_time
    - 1.450048 * daily_screen_time
    - 0.019252 * caffeine_intake
    + 4.710058 * exercise_high
    - 9.761921 * exercise_low
)

# -------------------------------
# Display Result
# -------------------------------
st.subheader("📊 Predicted Cognitive Ability Score")
st.metric(label="Cognitive Score", value=f"{cognitive_score:.2f}")

if cognitive_score >= 100:
    st.success("🟢 Cognitive Ability is classified as **High**.")
else:
    st.warning("🟠 Cognitive Ability is classified as **Low**.")

# -------------------------------
# QR Code (Update after deploy)
# -------------------------------
deployed_url = "https://your-app-url.streamlit.app"  # Replace after deploy

qr = qrcode.make(deployed_url)
qr_path = "qr_code.png"
qr.save(qr_path)

st.subheader("📱 Scan QR to open the app:")
st.image(Image.open(qr_path), width=200)
