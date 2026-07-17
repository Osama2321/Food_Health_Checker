# 🍎 Food Health Checker  
### 🚀 ML + FastAPI + Gradio | Production-Ready AI App

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/Gradio-UI-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/ML-Pipeline-red?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">

</p>

---

## 🌟 Overview

An **end-to-end Machine Learning application** that predicts whether a food item is:

| Health Status | Meaning |
|--------------|--------|
| 🟥 Unhealthy | High sugar/fat/sodium |
| 🟨 Moderate  | Balanced |
| 🟩 Healthy   | Nutritious |

---

## 🎯 Workflow

```mermaid
graph LR
A[User Input] --> B[Gradio UI]
B --> C[FastAPI Backend]
C --> D[ML Pipeline]
D --> E[Prediction]
E --> F[Result Display]

| Category         | Tools                    |
| ---------------- | ------------------------ |
| 🧠 ML            | Scikit-learn, SMOTE, PCA |
| ⚙️ Backend       | FastAPI                  |
| 🎨 Frontend      | Gradio                   |
| 📦 Model Storage | Joblib                   |
| 📊 Data          | USDA Food Nutrients      |


🧠 ML Pipeline
Imputer → Scaler → SMOTE → PCA → RandomForest

| Step    | Purpose               |
| ------- | --------------------- |
| Imputer | Handle missing values |
| Scaler  | Normalize features    |
| SMOTE   | Balance dataset       |
| PCA     | Reduce dimensions     |
| Model   | Predict health        |

| Feature  | Unit |
| -------- | ---- |
| Calories | kcal |
| Protein  | g    |
| Fat      | g    |
| Carbs    | g    |
| Sugar    | g    |
| Fiber    | g    |
| Sodium   | mg   |

📤 Output

{
  "prediction": "Healthy 🟩",
  "confidence": 0.87
}

📁 Project Structure

food-health-checker/
│
├── data/
│   └── food.csv
│
├── model/
│   └── pipeline.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── utils.py
│
├── app/
│   ├── api.py
│   └── gradio_app.py
│
├── requirements.txt
└── README.md


🚀 Quick Start
🔧 1. Clone Repo
git clone https://github.com/your-username/food-health-checker.git
cd food-health-checker

🧪 2. Setup Environment

python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

🧠 3. Train Model

python src/train.py

⚙️ 4. Run FastAPI
uvicorn app.api:app --reload

👉 API Docs:
http://127.0.0.1:8000/docs

🎨 5. Run Gradio UI

python app/gradio_app.py

<p align="center"> 🔥 Built with passion for Machine Learning 🚀 </p> ```