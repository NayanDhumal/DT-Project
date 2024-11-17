import streamlit as st
import pickle
import numpy as np

# Load your machine learning model (adjust the file name to match your model file)
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit app
st.title("Stroke Prediction Model Tester")

# User inputs
st.header("Enter Patient Data")

id = 20000
age = st.number_input("Age", min_value=0, step=1)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)

# Gender
gender = st.selectbox("Gender", ["Male", "Female"])
gender_Male = 1 if gender == "Male" else 0

# Ever married
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
ever_married_Yes = 1 if ever_married == "Yes" else 0

# Work type (Single attribute, not dummies)
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Children", "Government Job", "Never Worked"])

work_type_Private = 1 if work_type == "Private" else 0
work_type_Self_employed = 1 if work_type == "Self-employed" else 0
work_type_children = 1 if work_type == "Children" else 0
# Adding other work types as needed if present in your dataset

# Residence type
Residence_type_Urban = st.selectbox("Residence Type", ["Urban", "Rural"])
Residence_type_Urban = 1 if Residence_type_Urban == "Urban" else 0

# Smoking status
smoking_status = st.selectbox("Smoking Status", ["Formerly Smoked", "Never Smoked", "Smokes"])

smoking_status_formerly_smoked = 1 if smoking_status == "Formerly Smoked" else 0
smoking_status_never_smoked = 1 if smoking_status == "Never Smoked" else 0
smoking_status_smokes = 1 if smoking_status == "Smokes" else 0

# Reshape the inputs into the required format
input_data = np.array([[id,age, hypertension, heart_disease, avg_glucose_level, bmi, 
                        gender_Male, ever_married_Yes, work_type_Private, work_type_Self_employed, 
                        work_type_children, Residence_type_Urban, smoking_status_formerly_smoked, 
                        smoking_status_never_smoked, smoking_status_smokes]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Prediction: {prediction[0]}")


# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# model = pickle.load(open('model.pkl', 'rb'))

# # Function to predict stroke risk
# def predict_stroke_risk(patient_data):
#     patient_data = np.array(patient_data).reshape(1, -1)
#     prediction = model.predict(patient_data)
#     return prediction

# # Streamlit app
# st.title("Stroke Risk Prediction App")

# # Collect user input for patient data
# age = st.number_input("Age", min_value=1, max_value=120, value=25)
# hypertension = st.selectbox("Hypertension", (0, 1))  # 0: No, 1: Yes
# heart_disease = st.selectbox("Heart Disease", (0, 1))  # 0: No, 1: Yes
# avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=80.0)
# bmi = st.number_input("BMI", min_value=0.0, value=25.0)

# # You can add more inputs if necessary based on the features used by the model.

# # Predict button
# if st.button("Predict Stroke Risk"):
#     patient_data = [age, hypertension, heart_disease, avg_glucose_level, bmi]
#     prediction = predict_stroke_risk(patient_data)
    
#     if prediction[0] == 1:
#         st.error("High Risk of Stroke")
#     else:
#         st.success("Low Risk of Stroke")
