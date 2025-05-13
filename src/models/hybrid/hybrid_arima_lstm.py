
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
data_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
reports_path = os.path.join(project_root, "results", "reports")
os.makedirs(figs_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)

# Load data
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
df = df[["Close"]].dropna()

# --- Step 1: Fit ARIMA ---
arima_model = ARIMA(df["Close"], order=(1, 1, 1))
arima_results = arima_model.fit()
df["arima_forecast"] = arima_results.predict(start=0, end=len(df)-1)

# Drop initial NaNs
df.dropna(subset=["arima_forecast"], inplace=True)

# --- Step 2: Compute Residuals ---
df["residuals"] = df["Close"] - df["arima_forecast"]

# --- Step 3: LSTM on Residuals ---
residuals = df["residuals"].values.reshape(-1, 1)
scaler = MinMaxScaler()
scaled_residuals = scaler.fit_transform(residuals)

# Sequence generation
def create_sequences(data, window_size=60):
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i])
        y.append(data[i])
    return np.array(X), np.array(y)

window_size = 60
X, y = create_sequences(scaled_residuals, window_size)
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Build LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict residuals
predicted_scaled_residuals = model.predict(X_test)
predicted_residuals = scaler.inverse_transform(predicted_scaled_residuals)

# --- Step 4: Combine forecasts ---
arima_forecast_tail = df["arima_forecast"].values[-len(predicted_residuals):]
hybrid_forecast = arima_forecast_tail + predicted_residuals.flatten()
actual_tail = df["Close"].values[-len(predicted_residuals):]

# --- Step 5: Evaluate Hybrid ---
rmse = np.sqrt(mean_squared_error(actual_tail, hybrid_forecast))
mae = mean_absolute_error(actual_tail, hybrid_forecast)
mape = np.mean(np.abs((actual_tail - hybrid_forecast) / actual_tail)) * 100

print(f"Hybrid RMSE: {rmse:.2f}")
print(f"Hybrid MAE: {mae:.2f}")
print(f"Hybrid MAPE: {mape:.2f}%")

# Log metrics
metrics_file = os.path.join(reports_path, "Forecasting_Model_Metrics.csv")
metrics_df = pd.DataFrame([{
    "Model": "Hybrid_ARIMA_LSTM",
    "RMSE": round(rmse, 4),
    "MAE": round(mae, 4),
    "MAPE": round(mape, 2)
}])
if os.path.exists(metrics_file):
    existing = pd.read_csv(metrics_file)
    existing = existing[existing["Model"] != "Hybrid_ARIMA_LSTM"]
    full_df = pd.concat([existing, metrics_df], ignore_index=True)
else:
    full_df = metrics_df
full_df.to_csv(metrics_file, index=False)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(actual_tail, label="Actual")
plt.plot(hybrid_forecast, label="Hybrid Forecast", linestyle="--")
plt.title("Hybrid ARIMA + LSTM Forecast")
plt.legend()
plt.savefig(os.path.join(figs_path, "hybrid_arima_lstm_forecast.png"))
plt.close()
