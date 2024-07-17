import arimaModelConstruction as amc
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def create_sequences(data, seq_length):
        xs, ys = [], []
        for i in range(len(data)-seq_length):
            x = data[i:i+seq_length]
            y = data[i+seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)

def lstm_model_fit(data, forecast_length, test):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))

    seq_length = 10  # Example sequence length
    X, y = create_sequences(scaled_data, seq_length)

    # Define LSTM model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(seq_length, 1)),
        tf.keras.layers.LSTM(50),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train LSTM model
    try:
        model.fit(X, y, epochs=50, batch_size=32, verbose=0)
    except ValueError as ve:
        print(f"ValueError during model training: {ve}")
        return None

    # Forecast using LSTM
    lstm_forecast = []
    current_sequence = X[-1]
    for i in range(forecast_length):
        lstm_prediction = model.predict(current_sequence.reshape(1, seq_length, 1), verbose=0)[0, 0]
        lstm_forecast.append(lstm_prediction)
        current_sequence = np.roll(current_sequence, -1)
        current_sequence[-1] = lstm_prediction

    lstm_forecast = scaler.inverse_transform(np.array(lstm_forecast).reshape(-1, 1)).flatten()
    return lstm_forecast
    
def wa_hybrid_model_test(arima, lstm, test):
    least_mpe = 100    
    weighted_average = 0
    weighted_avg_ratio = 0
    for i in range(1, 1000):
        ratio = i / 1000
        test_ratio = ratio * arima['Forecast'] + (1-ratio) * lstm
        mse_test, mpe_test = amc.test_fit(test_ratio, test)
        
        if (abs(mpe_test) < abs(least_mpe)):
            least_mpe = mpe_test
            weighted_average = test_ratio
            weighted_avg_ratio = i/1000

    return weighted_average, weighted_avg_ratio