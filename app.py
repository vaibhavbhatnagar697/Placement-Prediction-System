import streamlit as st
import joblib
import numpy as np

model = joblib.load("placement_model.pkl")

st.title("Placement Package Prediction")

cgpa = st.number_input("CGPA")
dsa = st.number_input("DSA Score")
aptitude = st.number_input("Aptitude Score")
internships = st.number_input("Internships")
projects = st.number_input("Projects")

if st.button("Predict"):

    user_data = np.array([
        [
            cgpa,
            dsa,
            aptitude,
            internships,
            projects,
        ]
    ])

    prediction = model.predict(user_data)

    st.success(
        f"Predicted Package: {prediction[0]:.2f} LPA"
    )