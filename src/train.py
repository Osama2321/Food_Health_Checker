import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

from utils import health_score_rule

df = pd.read_csv("data/USDA.csv")

df["label"] = df.apply(health_score_rule, axis=1)

features = ['Calories', 'Protein', 'TotalFat', 'Carbohydrate', 'Sugar', 'Iron', 'Sodium']
X = df[features]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),  # 🔥 FIX
    ("scaler", StandardScaler()),
    ("smote", SMOTE(random_state=42)),
    ("pca", PCA(n_components=3)),
    ("model", RandomForestClassifier())
])


pipeline.fit(X_train, y_train)


os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/pipeline.pkl")

print("✅ Model trained successfully (NaN handled)")