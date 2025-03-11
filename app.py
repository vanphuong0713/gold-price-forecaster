from flask import Flask, render_template
from data_fetcher import fetch_gold_price_data
from forecaster import forecast_trend
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Lấy dữ liệu và dự báo
    data = fetch_gold_price_data()
    sma, forecast = forecast_trend(data)
    
    # Chuẩn bị dữ liệu cho giao diện
    dates = data.index.strftime('%Y-%m-%d').tolist()
    prices = data.tolist()
    sma_values = sma.tolist()
    forecast_dates = pd.date_range(start=dates[-1], periods=6, freq='B')[1:].strftime('%Y-%m-%d').tolist()  # 5 ngày tiếp theo
    forecast_values = forecast
    
    return render_template('index.html', 
                         dates=dates, prices=prices, 
                         sma=sma_values, forecast_dates=forecast_dates, 
                         forecast_values=forecast_values)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
