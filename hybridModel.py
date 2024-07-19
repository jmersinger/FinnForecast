import arimaModelConstruction as amc
import lstm

#Function to find the optimal weights for hybrid model
def wa_hybrid_model_test(arima, lstm, test, step):
    least_mpe = 100    
    weighted_average_forecast = 0
    weighted_avg_ratio = 0
    for i in range(0, step+1):
        ratio = i / step
        test_ratio = ratio * arima['Forecast'] + (1-ratio) * lstm
        mse_test, mpe_test = amc.test_fit(test_ratio, test)
        
        if (abs(mpe_test) < abs(least_mpe)):
            least_mpe = mpe_test
            weighted_average_forecast = test_ratio
            weighted_avg_ratio = i/step

    return weighted_average_forecast, weighted_avg_ratio

def hybrid_forecast(stock_data, forecast_length, arima_forecast, lstm_forecast, sequence_length, batch_size, epochs, step):
    #Calculate Optimized Hybrid Weights
    test_length = int(forecast_length/2)
    train, test = amc.split_training_data(stock_data, test_length)
    sample_arima_forecast = amc.arima_forecast(train, test_length)
    if (arima_forecast['Forecast'].isna().any()):
        print("Error: Something went wrong in Hybrid Weight ARIMA.")
    sample_lstm_forecast = lstm.lstm_model_fit(train, test_length, sequence_length, batch_size, epochs)
    if lstm_forecast is None:
        print("Error: Something went wrong in Hybrid Weight LSTM.")
    sample_hybrid_forecast, hybrid_weight = wa_hybrid_model_test(sample_arima_forecast, sample_lstm_forecast, test, step)
    print("[Loading]: Optimized Model Weights Calculated...")
    
    # Construct Hybrid Forecast
    hybrid_forecast = hybrid_weight * arima_forecast['Forecast'] + (1-hybrid_weight) * lstm_forecast          
    
    return hybrid_forecast

