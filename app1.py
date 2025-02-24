import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Streamlit UI
st.title("🥑 Avocado Region Prediction App")

# File uploader for the model
uploaded_model = st.file_uploader("Upload a trained model (Pickle file)", type=["pkl"])

def load_model(file):
    try:
        model = pickle.load(file)
        st.success("✅ Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Load the model if uploaded
model = load_model(uploaded_model) if uploaded_model else None

# Sidebar for user input features
st.sidebar.header("Enter Avocado Features")

average_price = st.sidebar.number_input("Average Price", min_value=0.0, value=1.5)
total_volume = st.sidebar.number_input("Total Volume", min_value=0.0, value=50000.0)
plu_4046 = st.sidebar.number_input("PLU 4046 Avocados", min_value=0.0, value=5000.0)
plu_4225 = st.sidebar.number_input("PLU 4225 Avocados", min_value=0.0, value=7000.0)
plu_4770 = st.sidebar.number_input("PLU 4770 Avocados", min_value=0.0, value=3000.0)
total_bags = st.sidebar.number_input("Total Bags", min_value=0.0, value=20000.0)
small_bags = st.sidebar.number_input("Small Bags", min_value=0.0, value=10000.0)
large_bags = st.sidebar.number_input("Large Bags", min_value=0.0, value=5000.0)
xlarge_bags = st.sidebar.number_input("XLarge Bags", min_value=0.0, value=1000.0)
type_ = st.sidebar.selectbox("Type", ["Conventional", "Organic"])
year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2022)

# Convert categorical values to numeric format
type_map = {"Conventional": 0, "Organic": 1}
type_ = type_map[type_]

# Convert inputs into a NumPy array
features = np.array([[average_price, total_volume, plu_4046, plu_4225, plu_4770, total_bags, small_bags, large_bags, xlarge_bags, type_, year]])

# Prediction button
if model and st.button("Predict Avocado Region"):
    try:
        prediction = model.predict(features)
        st.subheader(f"✅ Predicted Avocado Region: {prediction[0]}")
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")

