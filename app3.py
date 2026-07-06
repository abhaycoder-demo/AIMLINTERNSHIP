import streamlit as st
import tensorflow as tf
import joblib
import numpy as np

model = tf.keras.models.load_model("wine_model.keras")
scaler = joblib.load("scaler.pkl")

st.title("🍷 Wine Quality Prediction")

fixed_acidity = st.number_input("Fixed Acidity")
volatile_acidity = st.number_input("Volatile Acidity")
citric_acid = st.number_input("Citric Acid")
residual_sugar = st.number_input("Residual Sugar")
chlorides = st.number_input("Chlorides")
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide")
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide")
density = st.number_input("Density")
pH = st.number_input("pH")
sulphates = st.number_input("Sulphates")
alcohol = st.number_input("Alcohol")

if st.button("Predict"):

    sample = [[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
    ]]

    sample = scaler.transform(sample)

    pred = model.predict(sample)

    result = np.argmax(pred) + 3

    st.success(f"Predicted Wine Quality : {result}")