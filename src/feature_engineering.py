import pandas as pd
import os

from technical_indicators import (
    calculate_rsi,
    calculate_macd,
    bollinger_bands
)

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

files = [
    "AAPL.csv",
    "MSFT.csv",
    "GOOGL.csv",
    "NVDA.csv",
    "TSLA.csv"
]

for file in files:

    path = os.path.join(
        RAW_PATH,
        file
    )

    df = pd.read_csv(path)

    # Convert Date
    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    # Sort oldest to newest
    df = df.sort_values(
        by="Date"
    )

    # Close Price
    df["Close"] = (
        df["Price"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    # Volume Cleaning
    def clean_volume(v):

        v = str(v).strip()
    
        if "B" in v:
            return float(
                v.replace("B", "")
            ) * 1_000_000_000
    
        elif "M" in v:
            return float(
                v.replace("M", "")
            ) * 1_000_000
    
        elif "K" in v:
            return float(
                v.replace("K", "")
            ) * 1_000
    
        else:
            return float(
                v.replace(",", "")
            )

    df["Volume"] = (
        df["Vol."]
        .apply(clean_volume)
    )

    # Moving Averages
    df["MA10"] = (
        df["Close"]
        .rolling(10)
        .mean()
    )

    df["MA50"] = (
        df["Close"]
        .rolling(50)
        .mean()
    )

    # Returns
    df["Returns"] = (
        df["Close"]
        .pct_change()
    )

    # Volatility
    df["Volatility"] = (
        df["Returns"]
        .rolling(10)
        .std()
    )

    # RSI
    df["RSI"] = calculate_rsi(
        df["Close"]
    )

    # MACD
    df["MACD"] = calculate_macd(
        df["Close"]
    )

    # Bollinger Bands
    upper, lower = bollinger_bands(
        df["Close"]
    )

    df["UpperBand"] = upper
    df["LowerBand"] = lower

    df.dropna(inplace=True)

    output_file = os.path.join(
        PROCESSED_PATH,
        file.replace(
            ".csv",
            "_features.csv"
        )
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved {output_file}"
    )

print("Feature engineering completed")