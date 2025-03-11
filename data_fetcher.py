import yfinance as yf
import pandas as pd
from datetime import datetime
import time

def fetch_gold_price_data(max_retries=3):
    today = datetime.now().strftime('%Y-%m-%d')
    for attempt in range(max_retries):
        try:
            gold = yf.download('GC=F', start='2023-01-01', end=today, progress=False)
            return gold['Close']
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Chờ 2 giây trước khi thử lại
                continue
            raise Exception(f"Failed to fetch data after {max_retries} attempts: {str(e)}")
