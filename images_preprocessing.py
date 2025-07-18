from PIL import Image
import numpy as np

def preprocess(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((256, 256))
    img = np.array(img).astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img