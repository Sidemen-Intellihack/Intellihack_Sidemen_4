import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from datetime import datetime, timedelta
import os

# App title
st.title('Stock Market Prediction using LSTM')

# Sidebar input
st.sidebar.header('Stock Selection')
stock = st.sidebar.text_input('Enter Stock Symbol', 'AAPL')

# Use last 5 years data
start_date = datetime.today() - timedelta(days=365 * 5)
end_date = datetime.today()

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data(stock, start, end):
    data = yf.download(stock, start=start, end=end)
    data.reset_index(inplace=True)
    return data

data = load_data(stock, start_date, end_date)

# Show last 10 records
st.subheader('Stock Data')
st.write(data.tail(10))

# Fill missing values with rolling mean
def preprocess_data(data):
    data['Temp'] = data['Close'].rolling(window=5, min_periods=1).mean()
    data['Close'].fillna(data['Temp'], inplace=True)
    data.drop(columns=['Temp'], inplace=True)
    return data

data = preprocess_data(data)

# Scale data between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data[['Close']].values)

# Load model
MODEL_PATH = 'saved_model/stock_model.keras'
if not os.path.exists(MODEL_PATH):
    st.error("Model not found! Please add a trained model to the path.")
else:
    model = load_model(MODEL_PATH)
    st.success('Pre-trained model loaded successfully!')

# Predict next 5 days
def predict_next_5_days(model, scaled_data, seq_length=60):
    x_input = scaled_data[-seq_length:].reshape((1, seq_length, 1))
    predictions = []
    for _ in range(5):
        pred = model.predict(x_input)[0][0]
        predictions.append(pred)
        # update input with new pred
        pred = np.array(pred).reshape((1, 1, 1))
        x_input = np.append(x_input[:, 1:, :], pred, axis=1)
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return predictions

# Predict button
if st.sidebar.button('Predict Next 5 Days'):
    predictions = predict_next_5_days(model, scaled_data)

    # Create future dates
    future_dates = pd.date_range(start=data['Date'].iloc[-1], periods=6, freq='B')[1:]

    # Plot Results
    st.subheader('Prediction for Next 5 Days')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data['Date'], data['Close'], label='Actual Price', color='blue')
    ax.plot(future_dates, predictions, label='Predicted Price', color='red', marker='o')
    ax.legend()
    st.pyplot(fig)

    # Show predictions
    prediction_df = pd.DataFrame({'Date': future_dates, 'Predicted Close': predictions.flatten()})
    st.write(prediction_df)
