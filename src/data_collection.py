import yfinance as yf
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

ticker = "AAPL"

df = yf.download(
    ticker,
    period="5y",
    auto_adjust=True,
    progress=False
)

# Flatten multi-index columns
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df.reset_index(inplace=True)

print(df.head())

df.to_csv(
    f"data/raw/{ticker}.csv",
    index=False
)

print("Data saved successfully")