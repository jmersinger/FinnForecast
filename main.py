import fetchStockData as fsd
import arimaModelConstruction as amc

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def main():
    
    #Ticker Selection
    ticker = input("Please enter the stock ticker you want to forecast: ")
    print_csv = input("Would you like to save to raw stock data? (Y/N): ")
    forecast_length = int(input(f"How long (in months) do you want to forecast {ticker}: "))
    
    #Fetch data, build model, and test
    stock_data = fsd.fetch_and_clean(ticker, print_csv)
    amc.arima_forecast_test(stock_data, forecast_length)
    
    #LSTM Model
        
    

if __name__ == "__main__":
    main()