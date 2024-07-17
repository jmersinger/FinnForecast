import yfinance as yf
import pandas as pd

def delete_record(df, record_pk, filter_val, file):
    df = df[df[record_pk] != filter_val]
    df.to_csv(file)

def fetch_and_clean(ticker, print_csv):
    #Download & Clean Stock Data
    try:
        stock_data = yf.download(ticker, period="max", interval="1mo", progress=False)
    except KeyError as e:
        print(f"Error: {e}. Ticker symbol '{ticker}' not found or invalid.")
    if (print_csv == "Y"):
        stock_data.to_csv(f'./stockData/{ticker}.csv')   
    stock_data = stock_data.dropna()
    stock_data.index = pd.to_datetime(stock_data.index)
    stock_data = stock_data.sort_index()
    return stock_data