import testAvgMPE as fitTest
import hybridModel as hm


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
    # fitTest.average_measure_fits(12, 48, 20)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print("Hello! Welcome to FinnForecast! Please select an option:")
    print("(1) Create a simple forecast")
    print("(2) Create an advanced forecast")
    print("(3) Run a simple test")
    print("(4) Run an advanced test")
    mode = input()
    
    if mode == '1':
        print("Okay, lets make a simple forecast.")
        print("If you change your mind, just enter 'cancel' at any time to return to the menu.")
        # Ticker Selection
        ticker = input("Please enter the stock ticker you want to forecast: ")
        print_csv = input("Would you like to save to raw stock data? (Y/N): ")
        forecast_length = int(input(f"How long (in months) do you want to forecast {ticker}: "))        
        arima_forecast, lstm_forecast, hybrid_forecast = hm.hybrid_forecast(ticker, print_csv, forecast_length)
        
        print("ARIMA Forecast:")
        print(arima_forecast)
        print('\n')
        print("LSTM Forecast:")
        print(lstm_forecast)
        print('\n')
        print("Hybrid Forecast:")
        print(hybrid_forecast)
        print('\n')


        
    elif mode == '2':
        print("Okay, lets test.")
    else:
        print("Invaild selection. Please select and option (1 or 2).")
    
    # arima_forecast, lstm_forecast, hybrid_forecast = hm.hybrid_forecast('TSLA', 24)
    # print(arima_forecast)
    # print("\n\n\n")
    # print(lstm_forecast)
    # print("\n\n\n")
    # print(hybrid_forecast)

    

if __name__ == "__main__":
    main()