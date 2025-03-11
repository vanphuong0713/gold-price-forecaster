import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def fetch_gold_price_data():
    api_key = "YOUR_API_KEY"  # Thay bằng key từ Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=XAU&to_symbol=USD&apikey={api_key}"
    
    try:
        logger.info("Fetching gold price data from Alpha Vantage...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Ném lỗi nếu HTTP không thành công
        data = response.json()
        
        if "Time Series FX (Daily)" not in data:
            logger.error("Invalid response from Alpha Vantage")
            raise ValueError("No data returned from Alpha Vantage")
        
        time_series = data["Time Series FX (Daily)"]
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df = df['4. close'].astype(float)
        df.index = pd.to_datetime(df.index)
        logger.info(f"Fetched {len(df)} data points from Alpha Vantage")
        return df.sort_index()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to connect to Alpha Vantage: {str(e)}")
        raise Exception(f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    try:
        data = fetch_gold_price_data()
        print(data.tail())
    except Exception as e:
        print(f"Error: {str(e)}")
