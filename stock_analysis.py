import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical stock data for Apple
ticker = "AAPL"
data = yf.download(ticker, start="2022-01-01", end="2023-12-31")

# Show first few rows
print(data.head())

# Plot the closing price
plt.figure(figsize=(10, 5))
plt.plot(data['Close'])
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

