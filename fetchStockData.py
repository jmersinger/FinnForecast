import yfinance as yf
import pandas as pd

def delete_record(df, record_pk, filter_val, file):
    df = df[df[record_pk] != filter_val]
    df.to_csv(file)

def fetch_and_clean(ticker):
    #Download & Clean Stock Data
    try:
        stock_data = yf.download(ticker, period="max", interval="1mo", progress=False)
        stock_data = stock_data.dropna()
        stock_data.index = pd.to_datetime(stock_data.index)
        stock_data = stock_data.sort_index()
    except KeyError as e:
        stock_data = pd.DataFrame()
    except ValueError as e:
        stock_data = pd.DataFrame()  
    return stock_data