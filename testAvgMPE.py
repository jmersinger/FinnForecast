import fetchStockData as fsd
import arimaModelConstruction as amc
import pandas as pd

def calculate_Avg_MPE(forecast_length, test_range):
    yfin_stocks = pd.read_csv('stockTickers.csv')
    tickers = yfin_stocks['Ticker']
    MPEs = []
    index = 0
    for ticker in tickers.iloc:
        if index == test_range: break
        stock_data = fsd.fetch_and_clean(ticker, 'N')
        if stock_data.empty or yfin_stocks.shape[0] <= 12:
            yfin_stocks = yfin_stocks[yfin_stocks['Ticker'] != ticker]
            yfin_stocks.to_csv('stockTickers.csv')
            index -= 1
            continue
        mse, mpe = amc.arima_forecast_test(stock_data, forecast_length)
        MPEs.append(mpe)
        index += 1
        print(f"{index} Stocks Calculated...")
        
    
    avg_MPE = 0
    for mpe in MPEs:
        avg_MPE += mpe
    
    avg_MPE = avg_MPE / len(MPEs)
    
    return avg_MPE