import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import MinMaxScaler

# --- Paths ---
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
data_path = os.path.join(root, "data", "processed", "Tesla_Cleaned.csv")
lstm_model_path = os.path.join(root, "results", "models", "lstm_model.keras")
output_path = os.path.join(root, "results", "reports", "hybrid_forecast.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# --- Load Data ---
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
df = df[["Close"]].dropna()
train_size = int(0.8 * len(df))
train, test = df.iloc[:train_size], df.iloc[train_size:]

# --- Step 1: Fit ARIMA to get trend ---
arima_model = SARIMAX(train["Close"], order=(1, 1, 1))
arima_fit = arima_model.fit(disp=False)

# --- Get residuals from training set ---
train_pred = arima_fit.fittedvalues
train_resid = train["Close"].iloc[1:] - train_pred.iloc[1:]

# --- Normalize residuals ---
scaler = MinMaxScaler()
train_resid_scaled = scaler.fit_transform(train_resid.values.reshape(-1, 1))

# --- Prepare sequences ---
def create_sequences(data, win=60):
    X = [data[i - win:i] for i in range(win, len(data))]
    return np.array(X)

X_train = create_sequences(train_resid_scaled)

# --- Predict residuals from LSTM ---
model = load_model(lstm_model_path)
resid_pred_scaled = model.predict(X_train)
resid_pred = scaler.inverse_transform(resid_pred_scaled).flatten()

# --- Align predictions with test set ---
trend_forecast = arima_fit.forecast(steps=len(test))
resid_forecast = resid_pred[-len(test):]
hybrid_forecast = trend_forecast.values + resid_forecast

# --- Save Output ---
result_df = pd.DataFrame({
    "Date": test.index,
    "Actual": test["Close"].values,
    "Forecast": hybrid_forecast
})
result_df.to_csv(output_path, index=False)
print(f"Hybrid forecast saved to: {output_path}")
