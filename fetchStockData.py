import yfinance as yf
import pandas as pd
import os

def delete_record(df, record_pk, filter_val, file):
    df = df[df[record_pk] != filter_val]
    df.to_csv(file)

def fetch_and_clean(ticker, print_csv):
    #Download & Clean Stock Data
    path = "./output"
    folder_name = os.path.join(path, f"{ticker}_forecast")
    i = 1
    while os.path.exists(folder_name):
        folder_name = os.path.join(path, f"{ticker}_forecast_{i}")
        i += 1
    os.makedirs(folder_name)
    try:
        stock_data = yf.download(ticker, period="max", interval="1mo", progress=False)
    except KeyError as e:
        print(f"Error: {e}. Ticker symbol '{ticker}' not found or invalid.")
    if (print_csv == "Y"):
        stock_data.to_csv(f'{folder_name}/{ticker}_raw_data.csv')               
    stock_data = stock_data.dropna()
    stock_data.index = pd.to_datetime(stock_data.index)
    stock_data = stock_data.sort_index()
    return stock_data, folder_name