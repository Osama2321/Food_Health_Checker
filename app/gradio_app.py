import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/predict"

def check_health(calories, protein, fat, carbs, sugar, fiber, sodium):
    payload = {
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "sugar": sugar,
        "fiber": fiber,
        "sodium": sodium
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        return response.json()["prediction"]
    else:
        return "Error connecting to API"

demo = gr.Interface(
    fn=check_health,
    inputs=[
        gr.Number(label="Calories"),
        gr.Number(label="Protein (g)"),
        gr.Number(label="Fat (g)"),
        gr.Number(label="Carbs (g)"),
        gr.Number(label="Sugar (g)"),
        gr.Number(label="Fiber (g)"),
        gr.Number(label="Sodium (mg)")
    ],
    outputs="text",
    title="🍎 Food Health Checker",
    description="Enter nutrition values to check if your food is healthy"
)

if __name__ == "__main__":
    demo.launch()