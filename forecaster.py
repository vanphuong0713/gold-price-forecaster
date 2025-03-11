import pandas as pd
import numpy as np

def forecast_trend(data, window=20, forecast_days=5):
    if len(data) < window:
        raise ValueError(f"Not enough data points ({len(data)}) for window size {window}")
    sma = data.rolling(window=window).mean()
    last_sma = sma[-1] if not pd.isna(sma[-1]) else data[-1]  # Dùng giá cuối nếu SMA bị NaN
    forecast = [last_sma] * forecast_days
    return sma, forecast
