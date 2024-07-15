import yfinance as yf
import pandas as pd
from pmdarima import auto_arima

def main():
    
    #Ticker Selection
    ticker = input("Please enter the stock ticker you want to forecast: ")
    print_csv = input("Would you like to save to raw stock data? (Y/N): ")
    
    
    #Download & Clean Stock Data
    stock_data = yf.download(ticker)
    if (print_csv == "Y"):
        stock_data.to_csv(f'./stockData/{ticker}.csv')   
    stock_data = stock_data.dropna()
    
    

if __name__ == "__main__":
    main()