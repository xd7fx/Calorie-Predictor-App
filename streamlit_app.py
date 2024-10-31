import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('trained_model_calories.sav', 'rb'))

# Title of the app
st.title('Calorie Burn Prediction')

# Input fields for each feature
gender = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
age = st.number_input('Age', min_value=0, max_value=100, step=1)
height = st.number_input('Height (cm)', min_value=50.0, max_value=250.0, step=0.1)
weight = st.number_input('Weight (kg)', min_value=20.0, max_value=200.0, step=0.1)
duration = st.number_input('Duration (minutes)', min_value=0.0, max_value=300.0, step=0.1)
heart_rate = st.number_input('Heart Rate (bpm)', min_value=30.0, max_value=200.0, step=0.1)
body_temp = st.number_input('Body Temperature (°C)', min_value=30.0, max_value=45.0, step=0.1)

# Prepare input data
input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

# Prediction button
if st.button('Predict Calories'):
    # Make prediction
    prediction = model.predict(input_data)
    st.success(f'Predicted Calories Burned: {prediction[0]:.2f} kcal')
