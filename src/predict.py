import joblib
import pandas as pd

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

def predict_next_price(df):

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

    prediction = model.predict(X)

    return float(prediction[0])