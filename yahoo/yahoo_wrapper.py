import yfinance as yf
import time

ticker = yf.Ticker('AMZN')
data = ticker.info
print(dir(ticker))
print(dir(data))

print(ticker._price_history)


