import pandas as pd
import joblib

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

def forecast_next_7_days(df):

    latest = df.iloc[-1].copy()

    current_price = latest["Close"]

    predictions = []

    for day in range(1, 8):

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

        pred = model.predict(X)[0]

        predictions.append(
            {
                "Day": f"Day {day}",
                "Predicted Price": round(pred, 2)
            }
        )

        latest["Returns"] = (
            pred - current_price
        ) / current_price

        latest["MA10"] = (
            latest["MA10"] * 9 + pred
        ) / 10

        latest["MA50"] = (
            latest["MA50"] * 49 + pred
        ) / 50

        current_price = pred

    return pd.DataFrame(
        predictions
    )