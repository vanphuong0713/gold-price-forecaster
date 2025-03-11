import yfinance as yf
import pandas as pd

def fetch_gold_price_data():
    # Lấy dữ liệu giá vàng (GC=F là mã vàng tương lai)
    gold = yf.download('GC=F', start='2023-01-01', end='2025-03-10', progress=False)
    return gold['Close']  # Chỉ lấy giá đóng cửa
