import pandas as pd

def calculate_rsi(series, window=14):

    delta = series.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window).mean()

    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(series):

    ema12 = series.ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = series.ewm(
        span=26,
        adjust=False
    ).mean()

    return ema12 - ema26


def bollinger_bands(series):

    sma = series.rolling(20).mean()

    std = series.rolling(20).std()

    upper = sma + 2 * std

    lower = sma - 2 * std

    return upper, lower