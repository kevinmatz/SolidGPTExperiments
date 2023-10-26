from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/stock', methods=['POST'])
def stock():
   ticker = request.form['ticker']
   start_date = datetime(datetime.now().year, 1, 1)
   end_date = datetime.now()
   data = yf.download(ticker, start=start_date, end=end_date)
   data['Return'] = (1 + data['Close'].pct_change()).cumprod()
   plt.figure(figsize=(14, 7))
   plt.plot(data['Return'], 'r', label=ticker)
   plt.title('Stock Price Change YTD')
   plt.xlabel('Date')
   plt.ylabel('Cumulative Return')
   plt.legend()
   plt.grid(True)
   plt.savefig('static/stock_graph.png')  # Save the graph as a static file
   return render_template('stock.html')
