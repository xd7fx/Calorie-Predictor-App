# 🔥 Calories and Exercise Predictor

This Streamlit app leverages a 🔍 **Linear Regression** model to predict 🔥 **calories burned** based on various 🏃 **exercise metrics**. It serves as a starting point for exploring predictive modeling for 🏋️ **health and fitness** data.

## 🚀 Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://calorie-predictor-app.streamlit.app)


![image](https://github.com/user-attachments/assets/64231c0a-b5a4-4112-a383-ca5fbbe730bf)
![image](https://github.com/user-attachments/assets/93c92a7b-0cd9-4366-8b7c-6ea6d32134d5)


## 💻 GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/calories-exercise-predictor?quickstart=1)

## ✨ Features

- 📈 **Linear Regression Model**: Predicts calories burned based on exercise data.
- 📊 **Data Exploration**: Visualizes relationships between features (e.g., time spent on exercise, intensity) and calories burned.
- ✏️ **User Input**: Allows users to input custom data to make predictions using the model.

## 🔍 Model Information

The app uses a `LinearRegression` model to analyze the provided exercise data (`calories_and_exercis.ipynb`) and predict calories burned. The model is trained using variables such as:

- ⏱️ **Exercise Duration**
- 💪 **Exercise Intensity**
- ➕ **Other features (as available in the dataset)**

The dataset and model training are integrated within the app, allowing for real-time predictions.

**## 📈 Model Comparison and Accuracy

| 🤖 Model                 | 🎯Accuracy Score|
|--------------------------|------------------|
| Logistic Regression      | 96.04%           |
| Random Forest Classifier | 99.82%           |
| Support Vector Machine   | 99.13%           |
| K-Nearest Neighbors      | 99.36%           |
| Decision Tree Classifier | 99.35%           |

Based on this comparison, the **Random Forest Classifier** achieved the highest accuracy (99.82%) and was chosen as the primary model for this application. This model leverages multiple decision trees to improve prediction performance, making it a reliable choice for this task.
**

## 📚 Further Reading

- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- 🧠 [Scikit-Learn: Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- 🌐 [calories Dataset](https://github.com/xd7fx/Calorie-Predictor-App/blob/master/calories.csv)
- 🌐 [exercise Dataset](https://github.com/xd7fx/Calorie-Predictor-App/blob/master/exercise.csv)
