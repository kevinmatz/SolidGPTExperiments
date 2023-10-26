# filename: stock_data_plot_yfinance.py
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Fetch data
start_date = datetime(datetime.now().year, 1, 1)
end_date = datetime.now()

nvda = yf.download('NVDA', start=start_date, end=end_date)
tesla = yf.download('TSLA', start=start_date, end=end_date)
ibm = yf.download('IBM', start=start_date, end=end_date)

# Calculate the cumulative product of the daily returns
nvda['Return'] = (1 + nvda['Close'].pct_change()).cumprod()
tesla['Return'] = (1 + tesla['Close'].pct_change()).cumprod()
ibm['Return'] = (1 + ibm['Close'].pct_change()).cumprod()

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(nvda['Return'], 'r', label='NVIDIA')
plt.plot(tesla['Return'], 'b', label='TESLA')
plt.plot(ibm['Return'], 'g', label='IBM')
plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.savefig('static/stock_graph.png')
plt.show()