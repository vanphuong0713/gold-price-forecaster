import yfinance as yf
import pandas as pd
from datetime import datetime
import time
import logging

# Thiết lập logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def fetch_gold_price_data(max_retries=3):
    today = datetime.now().strftime('%Y-%m-%d')
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1}: Fetching gold price data from yfinance...")
            gold = yf.download('GC=F', start='2023-01-01', end=today, progress=False)
            if gold.empty:
                logger.warning("Received empty data from yfinance")
                raise ValueError("No data returned from Yahoo Finance")
            logger.info(f"Successfully fetched {len(gold)} data points")
            return gold['Close']
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Chờ 2 giây trước khi thử lại
                continue
            raise Exception(f"Failed to fetch gold price data after {max_retries} attempts: {str(e)}")

if __name__ == "__main__":
    try:
        data = fetch_gold_price_data()
        print(data.tail())
    except Exception as e:
        print(f"Error: {str(e)}")
