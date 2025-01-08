# Real Time Financial Data Dashboard

## Overview

This project provides an easy way to visualize and analyze stock price data in real-time. It fetches intraday stock prices from Alpha Vantage using their API and visualizes them using Python's `matplotlib`. Additionally, it calculates basic statistics (average, min, max prices) for the fetched data. This project is perfect for anyone who wants to get started with stock price analysis using Python.

## Features

- **Real-Time Stock Price Data**: Fetches intraday stock prices using the Alpha Vantage API.
- **Visualization**: Plots stock prices over time with interactive graphs using `matplotlib`.
- **Basic Analysis**: Computes and displays basic statistics (average price, min price, max price) for the selected stock.
- **User-Friendly Interface**: Allows users to input stock symbols and view the corresponding analysis.

## Requirements

Before you can run the application, ensure you have Python 3.x installed along with the required dependencies:

- `requests` for fetching data from the Alpha Vantage API.
- `matplotlib` for plotting the stock prices.
- `numpy` for numerical operations like calculating the average, min, and max prices.

Install the necessary Python libraries:

```bash
pip install requests matplotlib numpy
```

You will also need a **free Alpha Vantage API key**. You can get one by signing up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/RealTimeFinancialDataDashboard.git
   cd RealTimeFinancialDataDashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an Alpha Vantage API key**:
   - Sign up for a free API key at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
   - Replace the `api_key` in the script with your key or configure it as an environment variable.

## Usage

To run the project:

1. Clone the repository and install the required dependencies (as mentioned above).
2. Run the script:
   ```bash
   python main.py
   ```

3. Enter the stock symbol when prompted (e.g., `AAPL` for Apple):
   ```bash
   Enter stock symbol (e.g., AAPL): AAPL
   ```

4. The program will fetch the stock price data for the given symbol, perform statistical analysis, and generate a plot showing the stock prices over time.

## File Structure

```
RealTimeFinancialDataDashboard/
│
├── main.py  # Main script for fetching data and visualization
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

By: Adithya Sai Srinivas

---
