import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def connect_data(actual_data, forecast):
    # Connect Data
    last_record = actual_data.iloc[-1]
    last_record_series = pd.Series([last_record], index=[forecast.index[0]-pd.DateOffset(months=1)])
    connected_series = pd.concat([last_record_series, forecast])
    return connected_series

def plot_all(df):
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x=df.index, y='Actual', label='Actual', color='black')
    sns.lineplot(data=df, x=df.index, y='ARIMA_Forecast', label='ARIMA Forecast', color='green')
    sns.lineplot(data=df, x=df.index, y='LSTM_Forecast', label='LSTM Forecast', color='blue')
    sns.lineplot(data=df, x=df.index, y='Hybrid_Forecast', label='Hybrid Forecast', color='red')
    
    plt.title('Stock Price Forecasts')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    return plt.gcf()
    
def plot_single(df, column_name, color):
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x=df.index, y='Actual', label='Actual', color='black')
    sns.lineplot(data=df, x=df.index, y=column_name, label=column_name, color=color)
    
    plt.title('Stock Price Forecasts')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    return plt.gcf()
    

def plot_forecasts(stock_data, arima_forecast, lstm_forecast, hybrid_forecast):
    plot_range = len(arima_forecast)*3
    actual_len = len(arima_forecast)*2
    actual_data = stock_data['Close'].loc[stock_data.index[-actual_len:]]
    
    con_arima = connect_data(actual_data, arima_forecast['Forecast'])
    con_lstm = connect_data(actual_data, lstm_forecast)
    con_hybrid = connect_data(actual_data, hybrid_forecast)
    
    forecast_df = pd.DataFrame({
        'Actual': actual_data,
        'ARIMA_Forecast': con_arima,
        'LSTM_Forecast': con_lstm,
        'Hybrid_Forecast': con_hybrid
    }, index=pd.date_range(start=actual_data.index[0], periods=plot_range, freq='MS'))
    
    all = plot_all(forecast_df)
    arima = plot_single(forecast_df, 'ARIMA_Forecast', 'green')
    lstm = plot_single(forecast_df, 'LSTM_Forecast', 'blue')
    hybrid = plot_single(forecast_df,'Hybrid_Forecast', 'red')
    
    
    
    return all, arima, lstm, hybrid