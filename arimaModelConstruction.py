from pmdarima import auto_arima
from pmdarima.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error

def split_training_data(data, forecast_length):
    train, test = train_test_split(data['Close'], train_size=(data.shape[0]-forecast_length))
    return train, test

def mean_percentage_error(y_true, y_pred):
    return ((y_true - y_pred) / y_true).mean() * 100

def test_fit(forecast, test):
    try:
        mse = mean_squared_error(test, forecast)
        mpe = mean_percentage_error(test, forecast)
    except ValueError as e:
        print(f"Error: {e}. NaN value detected in forecast.")
        return None, None
        
    return mse, mpe


def arima_forecast(data, forecast_length):
    model = auto_arima(data, seasonal=False, error_action="ignore")
    forecast, conf_int = model.predict(n_periods=forecast_length, return_conf_int=True)
    
    forecast_index = pd.date_range(start=data.index[-1] + pd.DateOffset(months=1), periods=forecast_length, freq='MS')
    forecast_df = pd.DataFrame({
        'Forecast': forecast, 
        'Lower': conf_int[:, 0], 
        'Upper': conf_int[:, 1]
    }, index=forecast_index)
    
    forecast_csv_filename = "arima_forecast.csv"
    forecast_df.to_csv(forecast_csv_filename)
    
    return forecast_df

    
def arima_forecast_test(data, forecast_length):
    #ARIMA Model contruction
    train, test = split_training_data(data, forecast_length)
    forecast_df = arima_forecast(train, forecast_length)
    
    #Calculate MSE and MPE
    mse, mpe = test_fit(forecast_df['Forecast'], test)
        
    return mse, mpe
