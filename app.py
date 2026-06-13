import streamlit as st 
import joblib
import numpy as np 
import pandas as pd

# Import Saved model
model =joblib.load("gb_booking_model.pkl")

st.title("HOtel Booking Cancellation Predictor App")

st.divider()

st.write("Enter you booking details to predict cancellatoion")

st.divider()

lead_time = st.slider("Lead Time", 0, 500, 50)
avg_price = st.number_input("Average Price Per Room", 0, 500, 100)
special_requests = st.slider("number of Special Requests", 0.5,1.0)
total_guests = st.slider("Total Guests", 1, 10,2)
total_nights = st.slider("Total",1,20,3)
repreated_guest = st.selectbox("Repeated Guest", [0,1])

if st.button("Predict"):
    
    input_data = np.array([[
        lead_time,
        avg_price,
        special_requests,
        total_guests,
        total_nights,
        repreated_guest
          ]])
    
    
prediction = model.predict(input_data)[0]

proba = model.predict_proba(input_data)[0]

not_canceled_prob = proba[0]
canceled_prob = proba[1]

if prediction == 1:
    st.error(f"Prediction: Canceled (With Probability: {canceled_prob:.2%})")
else:
    st.success(f"Prediction: Not Canceled (With Probability: {not_canceled_prob:.2%})")
    
    
    # prediction = model.predict(input_data)[0]
    # prob = model.predict_proba(input_data)[0]
    
    
    # if prediction == 1:
    #     st.suucess(f"Prediction: Not Cancled (Probability:{prob:.2f})")
        
    # else:
    #     st.error(f"Prediction: Canceled (Probability: {1-prob:.2f}")