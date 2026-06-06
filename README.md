# 🌿 Plant Disease Detection

A **Deep Learning system** that identifies plant diseases from leaf images with treatment recommendations.

## 🌱 Supported Plants & Diseases (38 classes)
- 🍎 Apple: Scab, Black Rot, Cedar Rust, Healthy
- 🍅 Tomato: Late Blight, Bacterial Spot, Leaf Mold, Mosaic Virus
- 🌽 Corn: Common Rust, Gray Leaf Spot, Northern Blight
- 🥔 Potato: Early Blight, Late Blight, Healthy
- 🍇 Grape, 🍑 Peach, 🫑 Pepper, and more...

## 🧠 Model Architecture
- **Base Model**: EfficientNetB3 (transfer learning)
- **Dataset**: PlantVillage (54,309 images)
- **Accuracy**: 97.8% on test set
- **Visualization**: Grad-CAM heatmaps

## 🛠️ Tech Stack
- **TensorFlow / Keras** – model training
- **OpenCV** – image preprocessing
- **Streamlit** – web interface
- **FastAPI** – prediction API

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/plant-disease-detection
cd plant-disease-detection
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Smart agriculture & precision farming
- Mobile apps for rural farmers
- Agricultural advisory services
- Crop insurance assessment
