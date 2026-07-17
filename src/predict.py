import joblib
import numpy as np

MODEL_PATH = "model/pipeline.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_food(features):
    model = load_model()
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]