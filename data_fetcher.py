import yfinance as yf
import pandas as pd
from datetime import datetime
import time
import logging
import requests

# Thiết lập logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_internet_connection():
    """Kiểm tra kết nối mạng"""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def fetch_gold_price_data(max_retries=3, delay=2):
    if not check_internet_connection():
        logger.error("No internet connection available")
        raise ConnectionError("Cannot connect to the internet")
    
    today = datetime.now().strftime('%Y-%m-%d')
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1}/{max_retries}: Fetching gold price data from yfinance...")
            gold = yf.download('GC=F', start='2023-01-01', end=today, progress=False, timeout=10)
            if gold.empty:
                logger.warning("Received empty data from yfinance")
                raise ValueError("No data returned from Yahoo Finance")
            logger.info(f"Successfully fetched {len(gold)} data points")
            return gold['Close']
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                continue
            raise Exception(f"Failed to fetch gold price data after {max_retries} attempts: {str(e)}")

if __name__ == "__main__":
    try:
        data = fetch_gold_price_data()
        print(data.tail())
    except Exception as e:
        print(f"Error: {str(e)}")
