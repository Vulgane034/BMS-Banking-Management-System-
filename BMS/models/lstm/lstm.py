import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(32, input_shape=input_shape),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm(X_train, y_train, X_val, y_val, epochs=20, input_shape=None):
    if input_shape is None:
        input_shape = (X_train.shape[1], X_train.shape[2])
    model = create_lstm_model(input_shape)
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, verbose=0)
    return model

def predict_lstm(model, X):
    return model.predict(X).flatten()
