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

def lstm_model_fit(data, forecast_length):
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