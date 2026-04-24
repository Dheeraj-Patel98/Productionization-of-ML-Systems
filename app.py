
import gradio as gr
import joblib
import os
import numpy as np

# Load model and encoders
model_path = "model/xgb_flight_price_model.joblib"
from_enc = joblib.load("model/from_label_encoder.joblib")
to_enc = joblib.load("model/to_label_encoder.joblib")
agency_enc = joblib.load("model/agency_label_encoder.joblib")
type_enc = joblib.load("model/flightType_label_encoder.joblib")
model = joblib.load(model_path)

def predict_price(origin, destination, agency, flight_type, time, distance):
    try:
        # Encode categorical inputs
        origin_enc = from_enc.transform([origin])[0]
        destination_enc = to_enc.transform([destination])[0]
        agency_enc_val = agency_enc.transform([agency])[0]
        type_enc_val = type_enc.transform([flight_type])[0]

        # Prepare features
        features = np.array([[origin_enc, destination_enc, agency_enc_val, type_enc_val, time, distance]])

        # Predict
        prediction = model.predict(features)[0]
        return f"Predicted Flight Price: ₹{prediction:.2f}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Unique options from encoders
origins = from_enc.classes_.tolist()
destinations = to_enc.classes_.tolist()
agencies = agency_enc.classes_.tolist()
flight_types = type_enc.classes_.tolist()

# Gradio interface
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(origins, label="Origin"),
        gr.Dropdown(destinations, label="Destination"),
        gr.Dropdown(agencies, label="Agency"),
        gr.Dropdown(flight_types, label="Flight Type"),
        gr.Number(label="Flight Duration (minutes)"),
        gr.Number(label="Flight Distance (km)")
    ],
    outputs="text",
    title="✈️ Flight Price Prediction App",
    description="Enter flight details to get a predicted price using ML",
)

iface.launch()
