import fetchStockData as fsd
import arimaModelConstruction as amc
import testAvgMPE as test

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import models, layers
# from models import Sequential
# from layers import LSTM, Dense, Dropout

def main():
    
    #Ticker Selection
    # ticker = input("Please enter the stock ticker you want to forecast: ")
    # print_csv = input("Would you like to save to raw stock data? (Y/N): ")
    # forecast_length = int(input(f"How long (in months) do you want to forecast {ticker}: "))
    
    # #Fetch data, build model, and test
    # stock_data = fsd.fetch_and_clean(ticker, print_csv)
    # mse, mpe = amc.arima_forecast_test(stock_data, forecast_length)
    
    # print(f"Mean Squared Error (MSE): {mse}")
    # print(f"Mean Percentage Error (MPE): {mpe}%")
    
    #LSTM Model
    
    print(test.calculate_Avg_MPE(12, 500))
    

if __name__ == "__main__":
    main()