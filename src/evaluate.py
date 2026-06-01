import pandas as pd
import os
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.model_selection import train_test_split

import numpy as np

PROCESSED_PATH = "data/processed"

all_data = []

for file in os.listdir(PROCESSED_PATH):

    if file.endswith("_features.csv"):

        df = pd.read_csv(
            os.path.join(
                PROCESSED_PATH,
                file
            )
        )

        all_data.append(df)

dataset = pd.concat(
    all_data,
    ignore_index=True
)

features = [
    "MA10",
    "MA50",
    "Returns",
    "Volatility",
    "RSI",
    "MACD",
    "UpperBand",
    "LowerBand"
]

X = dataset[features]

y = dataset["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

results = []

for model_name in [
    "linear",
    "rf",
    "xgb"
]:

    model = joblib.load(
        f"models/{model_name}.pkl"
    )

    pred = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            pred
        )
    )

    r2 = r2_score(
        y_test,
        pred
    )

    results.append(
        [
            model_name,
            mae,
            rmse,
            r2
        ]
    )

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "MAE",
        "RMSE",
        "R2"
    ]
)

results_df.to_csv(
    "data/results.csv",
    index=False
)

print(results_df)