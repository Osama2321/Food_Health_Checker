from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

# Load model
MODEL_PATH = os.path.join("model", "pipeline.pkl")
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Food Health Checker API")

# Request schema
class FoodInput(BaseModel):
    calories: float
    protein: float
    fat: float
    carbs: float
    sugar: float
    fiber: float
    sodium: float


@app.get("/")
def home():
    return {"message": "Food Health Checker API is running 🚀"}


@app.post("/predict")
def predict(food: FoodInput):
    features = np.array([[
        food.calories,
        food.protein,
        food.fat,
        food.carbs,
        food.sugar,
        food.fiber,
        food.sodium
    ]])

    pred = model.predict(features)[0]

    label_map = {
        0: "Unhealthy 🟥",
        1: "Moderate 🟨",
        2: "Healthy 🟩"
    }

    return {
        "prediction": label_map[pred]
    }