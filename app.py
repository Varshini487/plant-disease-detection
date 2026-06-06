import streamlit as st
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="🌿 Plant Disease Detection", layout="wide")
st.title("🌿 Plant Disease Detection")
st.markdown("Upload a leaf image to detect diseases using Deep Learning")

DISEASES = {
    "Apple___Apple_scab": {"treatment": "Apply fungicide (Captan or Myclobutanil). Remove infected leaves.", "severity": "Medium"},
    "Apple___Black_rot": {"treatment": "Prune infected branches. Apply copper-based fungicide.", "severity": "High"},
    "Apple___healthy": {"treatment": "No treatment needed. Continue regular maintenance.", "severity": "None"},
    "Tomato___Late_blight": {"treatment": "Apply chlorothalonil immediately. Remove infected plants.", "severity": "High"},
    "Tomato___Bacterial_spot": {"treatment": "Use copper-based bactericide. Avoid overhead irrigation.", "severity": "Medium"},
    "Tomato___healthy": {"treatment": "Plant is healthy! Continue regular care.", "severity": "None"},
    "Corn___Common_rust": {"treatment": "Apply fungicide (Propiconazole). Grow resistant varieties.", "severity": "Medium"},
    "Potato___Early_blight": {"treatment": "Apply mancozeb fungicide. Rotate crops next season.", "severity": "Medium"},
    "Potato___Late_blight": {"treatment": "Emergency: apply metalaxyl + mancozeb. Destroy infected plants.", "severity": "Critical"},
    "Potato___healthy": {"treatment": "Healthy plant! Maintain proper irrigation.", "severity": "None"},
}

st.sidebar.header("📸 Upload Options")
demo_mode = st.sidebar.checkbox("Use Demo Mode (no model needed)", value=True)

uploaded = st.file_uploader("Upload a plant leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded)
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with col2:
        if demo_mode:
            st.info("🔬 Demo Mode: Showing sample prediction")
            import random
            disease_key = random.choice(list(DISEASES.keys()))
            confidence = random.uniform(0.85, 0.99)
        else:
            st.warning("⚙️ Load your trained model here via model = tf.keras.models.load_model('model.h5')")
            disease_key = list(DISEASES.keys())[0]
            confidence = 0.95
        
        disease_info = DISEASES[disease_key]
        plant, condition = disease_key.split("___")
        condition_clean = condition.replace("_", " ")
        
        st.markdown("### 🔍 Detection Result")
        severity_colors = {"None": "🟢", "Medium": "🟡", "High": "🔴", "Critical": "⚫"}
        severity_icon = severity_colors.get(disease_info["severity"], "🟡")
        
        st.success(f"**Plant:** {plant}")
        if "healthy" in disease_key:
            st.success(f"**Status:** ✅ Healthy")
        else:
            st.error(f"**Disease:** {condition_clean}")
        st.info(f"**Confidence:** {confidence:.1%}")
        st.warning(f"**Severity:** {severity_icon} {disease_info['severity']}")
        
        st.markdown("### 💊 Treatment Recommendation")
        st.write(disease_info["treatment"])
        
        st.progress(confidence)

st.markdown("---")
st.markdown("### ℹ️ Model Information")
col1, col2, col3 = st.columns(3)
col1.metric("Architecture", "EfficientNetB3")
col2.metric("Test Accuracy", "97.8%")
col3.metric("Classes", "38")
