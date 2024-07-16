import yfinance as yf
import pandas as pd


def fetch_and_clean(ticker, print_csv):
    #Download & Clean Stock Data
    stock_data = yf.download(ticker, period="max", interval="1mo")
    if (print_csv == "Y"):
        stock_data.to_csv(f'./stockData/{ticker}.csv')   
    stock_data = stock_data.dropna()
    stock_data.index = pd.to_datetime(stock_data.index)
    stock_data = stock_data.sort_index()
    return stock_data