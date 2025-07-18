import streamlit as st
from PIL import Image
import os
from plant_inference import predict

st.title("🌿 Plant Disease Classifier")

uploaded = st.file_uploader("Upload a plant leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    temp_path = "temp.jpg"
    image.save(temp_path)

    label, confidence = predict(temp_path)

    col1, col2, col3 = st.columns([1, 0.1, 1.2])

    with col1:
        st.image(image, caption="Prediction Image", use_container_width=True)

    with col3:
        st.text_area("🧾 Prediction Result", f"Class: {label}\nConfidence: {confidence:.2f}%")

    os.remove(temp_path)
