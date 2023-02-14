import numpy as np
import yfinance as yf

# Prompt the user for a stock symbol
symbol = input("Enter a stock symbol: ")

# Get the historical data for the stock
stock_data = yf.download(symbol, start="2010-01-01", end="2022-02-14")

# Calculate the 20-day moving average
stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()

# Create a new column that signals when to buy or sell
stock_data['Signal'] = 0
stock_data['Signal'][20:] = np.where(stock_data['Close'][20:] > stock_data['MA20'][20:], 1, 0)

# Calculate the daily returns based on the signal
stock_data['Returns'] = stock_data['Close'].pct_change() * stock_data['Signal'].shift(1)

# Calculate the cumulative returns
cumulative_returns = (1 + stock_data['Returns']).cumprod()

# Print the cumulative returns at the end of the period
print("Cumulative returns:", cumulative_returns[-1])
