import fetchStockData as fsd
import arimaModelConstruction as amc
import lstm
import pandas as pd

def wa_hybrid_model_test(arima, lstm, test):
    least_mpe = 100    
    weighted_average_forecast = 0
    weighted_avg_ratio = 0
    for i in range(0, 5001):
        ratio = i / 5000
        test_ratio = ratio * arima['Forecast'] + (1-ratio) * lstm
        mse_test, mpe_test = amc.test_fit(test_ratio, test)
        
        if (abs(mpe_test) < abs(least_mpe)):
            least_mpe = mpe_test
            weighted_average_forecast = test_ratio
            weighted_avg_ratio = i/5000

    return weighted_average_forecast, weighted_avg_ratio

def hybrid_forecast(ticker, forecast_length):
    # Fetch and Clean Data
    stock_data = fsd.fetch_and_clean(ticker, 'N')
    if stock_data.empty:
        print("Error: This ticker is not supported at this time. Please select a new ticker.")
    elif stock_data.shape[0] <= 12:
        print("Error: Not enough data for selected ticker.\nPlease select a new ticker or a shorter forecast length.")
    print("[Loading]: Stock Data Recieved...")
    
    # Construct ARIMA Model and Forecast
    arima_forecast = amc.arima_forecast(stock_data["Close"], forecast_length)
    if (arima_forecast['Forecast'].isna().any()):
        print("Error: Something went wrong in ARIMA.")
    print("[Loading]: ARIMA Forecast Complete...")
    
    #Construct LSTM Model and Forecast
    lstm_forecast = lstm.lstm_model_fit(stock_data['Close'], forecast_length)
    if lstm_forecast is None:
        print("Error: Something went wrong in LSTM.") 
    lstm_forecast = pd.Series(lstm_forecast, pd.date_range(start=stock_data.index[-1] + pd.DateOffset(months=1), periods=forecast_length, freq='MS'))
    print("[Loading]: LSTM Forecast Complete...")    
    
    #Calculate Optimized Hybrid Weights
    train, test = amc.split_training_data(stock_data, forecast_length)
    
    sample_arima_forecast = amc.arima_forecast(train, forecast_length)
    if (arima_forecast['Forecast'].isna().any()):
        print("Error: Something went wrong in Hybrid Weight ARIMA.")
    sample_lstm_forecast = lstm.lstm_model_fit(train, forecast_length)
    if lstm_forecast is None:
        print("Error: Something went wrong in Hybrid Weight LSTM.")
    sample_hybrid_forecast, hybrid_weight = wa_hybrid_model_test(sample_arima_forecast, sample_lstm_forecast, test)
    print("[Loading]: Optimized Model Weights Calculated...")
    
    
    # Construct Hybrid Forecast
    hybrid_forecast = hybrid_weight * arima_forecast['Forecast'] + (1-hybrid_weight) * lstm_forecast
    print("[Complete!]: Hybrid Forecast Complete...")
    
    return arima_forecast, lstm_forecast, hybrid_forecast

