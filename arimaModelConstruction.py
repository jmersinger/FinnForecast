from pmdarima import auto_arima
from pmdarima.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error

def mean_percentage_error(y_true, y_pred):
    return ((y_true - y_pred) / y_true).mean() * 100
    
def arima_forecast_test(data, forecast_length):
    #ARIMA Model contruction
    train, test = train_test_split(data['Close'], train_size=(data.shape[0]-forecast_length))
    model = auto_arima(train, seasonal=False)

    #Create Forecast    
    forecast, conf_int = model.predict(n_periods=forecast_length, return_conf_int=True)
        
    #Generate Forecast Index and DF
    forecast_index = pd.date_range(start=train.index[-1] + pd.DateOffset(months=1), periods=forecast_length, freq='MS')
    forecast_df = pd.DataFrame({
        'Forecast': forecast, 
        'Lower': conf_int[:, 0], 
        'Upper': conf_int[:, 1]
    }, index=forecast_index)
    
    forecast_csv_filename = "arima_forecast.csv"
    forecast_df.to_csv(forecast_csv_filename)
    
    #Calculate MSE
    mse = mean_squared_error(test, forecast_df['Forecast'])
    print(f"Mean Squared Error (MSE): {mse}")
    
    #Calculate MPE
    mpe = mean_percentage_error(test, forecast_df['Forecast'])
    print(f"Mean Percentage Error (MPE): {mpe}%")