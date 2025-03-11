import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_gold_price_data():
    today = datetime.now().strftime('%Y-%m-%d')
    gold = yf.download('GC=F', start='2023-01-01', end=today, progress=False)
    return gold['Close']
