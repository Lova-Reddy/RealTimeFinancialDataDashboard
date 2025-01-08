import requests
import matplotlib.pyplot as plt
import time
import numpy as np

# Fetching Data from Alpha Vantage API (Free Signup Required)
def fetch_stock_data(symbol, api_key="8DM5FXVIJS8H4YYW"):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "Time Series (1min)" not in data:
        print("Error fetching data:", data.get("Note", data))
        return []
    
    prices = []
    timestamps = []
    for time, stats in data["Time Series (1min)"].items():
        prices.append(float(stats["1. open"]))
        timestamps.append(time)
    
    return timestamps[::-1], prices[::-1]  # Reverse for chronological order

# Plotting and Analysis
def plot_stock_prices(timestamps, prices, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, label=f"{symbol} Prices")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.title(f"Stock Prices for {symbol}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

def calculate_statistics(prices):
    print("Basic Statistics:")
    print(f"Average Price: {np.mean(prices):.2f}")
    print(f"Min Price: {np.min(prices):.2f}")
    print(f"Max Price: {np.max(prices):.2f}")

# Main Execution
if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    api_key = "8DM5FXVIJS8H4YYW"  # Alpha Vantage API key
    timestamps, prices = fetch_stock_data(symbol, api_key)
    
    if prices:
        calculate_statistics(prices)
        plot_stock_prices(timestamps, prices, symbol)
