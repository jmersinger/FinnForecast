import arimaModelConstruction as amc
import lstm
import hybridModel as hm
import plot
import output
import pandas as pd

def forecast(ticker, stock_data, forecast_length, sequence_length=48, batch_size=64, epochs=75, step=100):
    print("[Loading]: Stock Data Recieved...")
    
    # Construct ARIMA Model and Forecast
    arima_forecast = amc.arima_forecast(stock_data["Close"], forecast_length)
    if (arima_forecast['Forecast'].isna().any()):
        print("Error: Something went wrong in ARIMA.")
    print("[Loading]: ARIMA Forecast Complete...")
    
    #Construct LSTM Model and Forecast
    lstm_forecast = lstm.lstm_model_fit(stock_data['Close'], forecast_length, sequence_length, batch_size, epochs)
    if lstm_forecast is None:
        print("Error: Something went wrong in LSTM.") 
    lstm_forecast = pd.Series(lstm_forecast, pd.date_range(start=stock_data.index[-1] + pd.DateOffset(months=1), periods=forecast_length, freq='MS'))
    print("[Loading]: LSTM Forecast Complete...")
    
    #Construct Hybrid Forecast
    hybrid_forecast = hm.hybrid_forecast(stock_data, forecast_length, arima_forecast, lstm_forecast, sequence_length, batch_size, epochs, step)
    if lstm_forecast is None:
        print("Error: Something went wrong in Hybrid Forecast.") 
    print("[Loading]: Hybrid Forecast Complete...")
    
    #Plot Forecasts
    plot_all, plot_arima, plot_lstm, plot_hybrid = plot.plot_forecasts(stock_data, arima_forecast, lstm_forecast, hybrid_forecast)
    print("[Loading]: Forecast Plot Complete...")
        
    #Output Data
    path = output.output_to_folder(ticker, stock_data, arima_forecast, lstm_forecast, hybrid_forecast, plot_all, plot_arima, plot_lstm, plot_hybrid)
    print(f'[Complete!]: Output printed to {path}')
