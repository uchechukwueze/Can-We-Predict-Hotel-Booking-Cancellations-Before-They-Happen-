import streamlit as st 
import joblib
import numpy as np 
import pandas as pd

# Import saved model
model = joblib.load("gb_booking_model.pkl")

st.title("Hotel Booking Cancellation Predictor App")

st.divider()

st.write("Enter your booking details to predict cancellation")

st.divider()

lead_time = st.slider("Lead Time", 0, 500, 50)
avg_price = st.number_input("Average Price Per Room", 0, 500, 100)
special_requests = st.slider("Number of Special Requests", 0, 5, 1)
total_guests = st.slider("Total Guests", 1, 10, 2)
total_nights = st.slider("Total Nights", 1, 20, 3)
repeated_guest = st.selectbox("Repeated Guest", [0, 1])

if st.button("Predict"):
    
    input_data = np.array([[
        lead_time,
        avg_price,
        special_requests,
        total_guests,
        total_nights,
        repeated_guest
    ]])
    
    prediction = model.predict(input_data)[0]

    proba = model.predict_proba(input_data)[0]

    not_canceled_prob = proba[0]
    canceled_prob = proba[1]

    if prediction == 1:
        st.error(f"Prediction: Canceled | Probability: {canceled_prob:.2%}")
    else:
        st.success(f"Prediction: Not Canceled | Probability: {not_canceled_prob:.2%}")