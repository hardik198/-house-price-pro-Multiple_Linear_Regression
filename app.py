import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    result = model.predict(input_data)

    st.success(f"Predicted Price: ₹ {int(result[0])}")