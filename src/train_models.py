import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor

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

models = {
    "linear": LinearRegression(),
    "rf": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    "xgb": XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5
    )
}

for name, model in models.items():

    model.fit(
        X_train,
        y_train
    )

    joblib.dump(
        model,
        f"models/{name}.pkl"
    )

    print(
        f"{name} model saved"
    )