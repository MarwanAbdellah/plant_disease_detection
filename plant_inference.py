import onnxruntime as ort
import numpy as np
import pandas as pd
from images_preprocessing import preprocess

df = pd.read_csv("data_warehouse.csv")
class_list = sorted(df["class"].unique())
idx_to_class = {i: class_name for i, class_name in enumerate(class_list)}       # For Class names

session = ort.InferenceSession("plant_disease_model.onnx")
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

def predict(img_path):
    img_arr = preprocess(img_path)
    result = session.run([output_name], {input_name: img_arr})
    raw_scores = result[0]
    prob_vals = np.exp(raw_scores) / np.sum(np.exp(raw_scores), axis=1, keepdims=True)
    top_idx = np.argmax(prob_vals, axis=1)[0]
    confidence = prob_vals[0][top_idx] * 100
    class_name = idx_to_class.get(top_idx, "Unknown")
    return class_name, confidence
