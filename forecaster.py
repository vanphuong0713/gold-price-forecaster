import pandas as pd
import numpy as np

def forecast_trend(data, window=20, forecast_days=5):
    # Tính trung bình động (SMA)
    sma = data.rolling(window=window).mean()
    
    # Dự báo đơn giản: lấy giá trị SMA cuối cùng làm xu hướng
    last_sma = sma[-1]
    forecast = [last_sma] * forecast_days  # Dự báo 5 ngày tiếp theo
    
    return sma, forecast
