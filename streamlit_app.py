import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('trained_model_calories.sav', 'rb'))

# Language setting
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def toggle_language():
    st.session_state.lang = "ar" if st.session_state.lang == "en" else "en"

# Language texts with decorations
texts = {
    "en": {
        "title": "🔥 Calorie Burn Prediction",
        "gender": "Gender",
        "male": "Male",
        "female": "Female",
        "age": "Age",
        "height": "Height (cm)",
        "weight": "Weight (kg)",
        "duration": "Duration (minutes)",
        "heart_rate": "Heart Rate (bpm)",
        "body_temp": "Body Temperature (°C)",
        "predict_button": "Predict Calories 🔥",
        "change_language": "Change Language 🌐",
        "success_message": "Predicted Calories Burned:"
    },
    "ar": {
        "title": "🔥 التنبؤ بحرق السعرات الحرارية",
        "gender": "الجنس",
        "male": "ذكر",
        "female": "أنثى",
        "age": "العمر",
        "height": "الطول (سم)",
        "weight": "الوزن (كجم)",
        "duration": "المدة (بالدقائق)",
        "heart_rate": "معدل ضربات القلب (نبضة في الدقيقة)",
        "body_temp": "درجة حرارة الجسم (°م)",
        "predict_button": "تنبؤ بالسعرات 🔥",
        "change_language": "تغيير اللغة 🌐",
        "success_message": "السعرات الحرارية المحروقة المتوقعة:"
    }
}

# Streamlit app title with language toggle button
st.title(texts[st.session_state.lang]["title"])
st.button(texts[st.session_state.lang]["change_language"], on_click=toggle_language)

# Input fields with labels based on selected language
gender = st.selectbox(texts[st.session_state.lang]["gender"],
                      options=[0, 1],
                      format_func=lambda x: texts[st.session_state.lang]["male"] if x == 1 else texts[st.session_state.lang]["female"])
age = st.number_input(texts[st.session_state.lang]["age"], min_value=0, max_value=100, step=1)
height = st.number_input(texts[st.session_state.lang]["height"], min_value=50.0, max_value=250.0, step=0.1)
weight = st.number_input(texts[st.session_state.lang]["weight"], min_value=20.0, max_value=200.0, step=0.1)
duration = st.number_input(texts[st.session_state.lang]["duration"], min_value=0.0, max_value=300.0, step=0.1)
heart_rate = st.number_input(texts[st.session_state.lang]["heart_rate"], min_value=30.0, max_value=200.0, step=0.1)
body_temp = st.number_input(texts[st.session_state.lang]["body_temp"], min_value=30.0, max_value=45.0, step=0.1)

# Prepare input data for prediction
input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

# Prediction button and result display
if st.button(texts[st.session_state.lang]["predict_button"]):
    # Make prediction
    prediction = model.predict(input_data)
    st.success(f'{texts[st.session_state.lang]["success_message"]} {prediction[0]:.2f} kcal')
