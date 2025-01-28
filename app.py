import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the saved model, encoder, and scaler
model = joblib.load('decision_tree_model.joblib')
disease_encoder = joblib.load('disease_encoder.joblib')
scaler = joblib.load('scaler.joblib')

# Function to predict based on user input
def predict_disease(data):
    # Apply the scaling
    continuous_columns = ['Density', 'BodyFat', 'Age', 'Weight', 'Height', 'Neck', 'Chest', 'Abdomen', 
                          'Hip', 'Thigh', 'Knee', 'Ankle', 'Biceps', 'Forearm', 'Wrist']
    data[continuous_columns] = scaler.transform(data[continuous_columns])
    
    # Make prediction
    prediction = model.predict(data)
    
    # Decode prediction to original disease label
    predicted_disease = disease_encoder.inverse_transform(prediction)
    return predicted_disease[0]

# Streamlit UI setup
st.set_page_config(page_title="Health Risk Predictor", page_icon="🏥", layout="wide")
st.title('Health Risk Prediction')
st.write("Enter the following details to predict health risks:")
col1, col2 = st.columns(2)


# Collecting user input
with col1:
    density = st.number_input("Density", min_value=0.5, max_value=1.5, value=1.1, step=0.01)
    body_fat = st.number_input("Body Fat (%)", min_value=0.0, max_value=50.0, value=22.0, step=0.1)
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70, step=1)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170, step=1)
    neck = st.number_input("Neck (cm)", min_value=30, max_value=60, value=37, step=1)
    chest = st.number_input("Chest (cm)", min_value=60, max_value=150, value=90, step=1)
    abdomen = st.number_input("Abdomen (cm)", min_value=50, max_value=150, value=85, step=1)
with col2:
    hip = st.number_input("Hip (cm)", min_value=50, max_value=150, value=90, step=1)
    thigh = st.number_input("Thigh (cm)", min_value=30, max_value=100, value=60, step=1)
    knee = st.number_input("Knee (cm)", min_value=30, max_value=100, value=40, step=1)
    ankle = st.number_input("Ankle (cm)", min_value=10, max_value=30, value=20, step=1)
    biceps = st.number_input("Biceps (cm)", min_value=20, max_value=50, value=35, step=1)
    forearm = st.number_input("Forearm (cm)", min_value=20, max_value=40, value=30, step=1)
    wrist = st.number_input("Wrist (cm)", min_value=10, max_value=30, value=18, step=1)
    gender = st.selectbox("Gender", options=["Male", "Female"])

# Prepare input data
input_data = {
    'Density': [density],
    'BodyFat': [body_fat],
    'Age': [age],
    'Weight': [weight],
    'Height': [height],
    'Neck': [neck],
    'Chest': [chest],
    'Abdomen': [abdomen],
    'Hip': [hip],
    'Thigh': [thigh],
    'Knee': [knee],
    'Ankle': [ankle],
    'Biceps': [biceps],
    'Forearm': [forearm],
    'Wrist': [wrist],
    'Gender': [0 if gender == 'Male' else 1]  # Convert gender to numeric (0: Male, 1: Female)
}

# Convert the input data to a DataFrame
input_df = pd.DataFrame(input_data)

# Predict and display the result
if st.button('Predict'):
    prediction = predict_disease(input_df)
    st.write(f"Predicted Disease Class: {prediction}")



