import fetchStockData as fsd
import arimaModelConstruction as amc
import testAvgMPE as fitTest
import lstm
import hybridModel as hm

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# from models import Sequential
# from layers import LSTM, Dense, Dropout

def main():
    
    # Ticker Selection
    # ticker = input("Please enter the stock ticker you want to forecast: ")
    # print_csv = input("Would you like to save to raw stock data? (Y/N): ")
    # forecast_length = int(input(f"How long (in months) do you want to forecast {ticker}: "))
    # ticker = 'TSLA'
    # print_csv = 'Y'
    # forecast_length = 12
    
    # # #Fetch data, build model, and test
    # stock_data = fsd.fetch_and_clean(ticker, print_csv)
    # train, test = amc.split_training_data(stock_data, forecast_length)
    # mse_arima, mpe_arima = amc.arima_forecast_test(stock_data, forecast_length)
    # arima_forecast = amc.arima_forecast(train, forecast_length)
    
    # print(f"Mean Squared Error (MSE): {mse_arima}")
    # print(f"Mean Percentage Error (MPE): {mpe_arima}%")
    
    # lstm_forecast = lstm.lstm_model(stock_data, forecast_length, test)
    
    
    # print(fitTest.calculate_Avg_MPE(12, 100))
    fitTest.average_measure_fits(12, 100)
    
    # print("Hello! Welcome to FinnForecast! Please select an option:")
    # print("(1) Create a forecast\n")
    # print("(2) Test model accuracy")
    
    # arima_forecast, lstm_forecast, hybrid_forecast = hm.hybrid_forecast('TSLA', 24)
    # print(arima_forecast)
    # print("\n\n\n")
    # print(lstm_forecast)
    # print("\n\n\n")
    # print(hybrid_forecast)

    

if __name__ == "__main__":
    main()