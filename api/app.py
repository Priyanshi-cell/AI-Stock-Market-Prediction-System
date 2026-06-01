from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(
    title="AI Stock Prediction API"
)

model = joblib.load(
    "models/linear.pkl"
)

FEATURES = [
    "MA10",
    "MA50",
    "Returns",
    "Volatility",
    "RSI",
    "MACD",
    "UpperBand",
    "LowerBand"
]

@app.get("/")
def home():

    return {
        "message":
        "AI Stock Prediction API"
    }

@app.get("/predict/{stock}")
def predict(stock: str):

    stock = stock.upper()

    df = pd.read_csv(
        f"data/processed/{stock}_features.csv"
    )

    latest = df.iloc[-1]

    X = pd.DataFrame(
        [[
            latest["MA10"],
            latest["MA50"],
            latest["Returns"],
            latest["Volatility"],
            latest["RSI"],
            latest["MACD"],
            latest["UpperBand"],
            latest["LowerBand"]
        ]],
        columns=FEATURES
    )

    prediction = model.predict(X)[0]

    return {
        "stock": stock,
        "prediction": round(
            float(prediction),
            2
        )
    }
@app.get("/")
def home():
    return {
        "project": "AI Powered Stock Market Prediction System",
        "author": "Priyanshi Kumrawat",
        "status": "running",
        "documentation": "/docs"
    }