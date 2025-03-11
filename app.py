import os
# ... (các import khác)

app = Flask(__name__)

@app.route('/')
def home():
    try:
        logger.info("Starting data fetch...")
        data = fetch_gold_price_data()
        # ... (phần còn lại giữ nguyên)
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}", exc_info=True)
        return f"Internal Server Error: {str(e)}", 500
