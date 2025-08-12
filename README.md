# 🌿 Plant Disease Detection

A deep learning project using **ResNet18**, **PyTorch**, **ONNX**, **Streamlit**, and **Docker** to detect plant diseases from images.

---

## 🚀 Features

- Trained using **ResNet18** from `torchvision.models`
- Exported model to **ONNX** for optimized inference
- Interactive web interface built with **Streamlit**
- Fully containerized using **Docker** with separate base and app Dockerfiles

---

## 🧠 Model Architecture

This project uses **ResNet18**, a convolutional neural network pretrained on ImageNet and fine-tuned for plant disease classification.

**Model Export to ONNX:**

```python
import torch.onnx

# Dummy input
x = torch.randn(1, 3, 256, 256)
torch.onnx.export(model, x, "model.onnx", input_names=['input'], output_names=['output'], ...)
```

---

## 🖥️ Streamlit Interface

Launch the Streamlit app to interact with the model via your browser. Users can upload a plant image and receive predictions instantly.

---

## 🐳 Docker Setup

The app is fully dockerized with a 2-stage setup:

1. **base.Dockerfile** – Sets up the base image with dependencies  
2. **app.Dockerfile** – Copies app files and runs the Streamlit server

**Build & Run:**

```bash
# Step 1: Build base image
docker build -f base.Dockerfile -t plant_base .

# Step 2: Build app image
docker build -f app.Dockerfile -t plant_app .

# Step 3: Run the app
docker run -p 8501:8501 plant_app
```

---

## 📁 Folder Structure

```text
├── app.py
├── model.onnx
├── base.Dockerfile
├── app.Dockerfile
├── utils/
│   └── predict.py
├── images/
│   └── sample_leaf.jpg
```

---

## 📝 License

MIT License. Feel free to use, share, and modify the project.
