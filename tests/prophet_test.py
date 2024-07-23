import pandas as pd
from prophet import Prophet
import sys
import os


def create_prophet_forecast(data, forecast_length):
    data = data.reset_index()
    data.columns = ['ds', 'y']
    
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    
    model = Prophet()
    model.fit(data)
    
    future_df = model.make_future_dataframe(periods=forecast_length, freq='MS')
    full_forecast = model.predict(future_df)

    forecast_start_date = data['ds'].max() + pd.DateOffset(months=1)    
    forecast = full_forecast[full_forecast['ds'] >= forecast_start_date][['ds', 'yhat']]
    
    # Set the 'ds' column as the datetime index
    forecast.set_index('ds', inplace=True)
    
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    
    return forecast