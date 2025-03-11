from flask import Flask, render_template
from data_fetcher import fetch_gold_price_data
from forecaster import forecast_trend
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    try:
        logger.info("Starting data fetch...")
        data = fetch_gold_price_data()
        if data.empty:
            logger.error("No data fetched from yfinance")
            return "Error: No gold price data available", 500
        
        logger.info("Calculating forecast...")
        sma, forecast = forecast_trend(data)
        
        logger.info("Preparing data for template...")
        dates = data.index.strftime('%Y-%m-%d').tolist()
        prices = data.tolist()
        sma_values = sma.tolist()
        forecast_dates = pd.date_range(start=dates[-1], periods=6, freq='B')[1:].strftime('%Y-%m-%d').tolist()
        forecast_values = forecast
        
        logger.info("Rendering template...")
        return render_template('index.html', 
                             dates=dates, prices=prices, 
                             sma=sma_values, forecast_dates=forecast_dates, 
                             forecast_values=forecast_values)
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}", exc_info=True)
        return f"Internal Server Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
