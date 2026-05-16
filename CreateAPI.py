from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load Model
model = joblib.load("diamond_price_model.pkl")

# Create App
app = FastAPI()

# Input Schema
class DiamondInput(BaseModel):

    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float
    volume: float

# Home Route
@app.get("/")
def home():

    return {
        "message": "Diamond Price Prediction API Running"
    }

# Prediction Route
@app.post("/predict")
def predict(data: DiamondInput):

    input_dict = {
        "carat": [data.carat],
        "cut": [data.cut],
        "color": [data.color],
        "clarity": [data.clarity],
        "depth": [data.depth],
        "table": [data.table],
        "x": [data.x],
        "y": [data.y],
        "z": [data.z],
        "volume": [data.volume]
    }

    df = pd.DataFrame(input_dict)

    prediction = model.predict(df)

    return {
        "predicted_price": float(prediction[0])
    }
