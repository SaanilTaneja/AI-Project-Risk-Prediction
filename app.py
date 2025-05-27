import streamlit as st
import pandas as pd
import joblib

st.title("🧠 AI Risk Predictor for IT Projects")

model = joblib.load("risk_model.pkl")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    mapping = {"Agile": 0, "Waterfall": 2, "Hybrid": 1}
    data['Methodology'] = data['Methodology'].map(mapping)

    st.write("📄 Uploaded Data:")
    st.dataframe(data)

    prediction = model.predict(data)
    risk_map = {0: "High", 1: "Low", 2: "Medium"}
    prediction_labels = [risk_map[p] for p in prediction]
    data["Predicted_Risk"] = prediction_labels

    st.write("🔮 Risk Predictions:")
    st.dataframe(data)
