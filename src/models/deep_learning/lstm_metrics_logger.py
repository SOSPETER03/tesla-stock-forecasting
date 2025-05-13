
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

# --- Paths ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
data_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
reports_path = os.path.join(project_root, "results", "reports")
models_path = os.path.join(project_root, "results", "models")

os.makedirs(figs_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)
os.makedirs(models_path, exist_ok=True)

# --- Load and preprocess data ---
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
df = df[["Close"]].dropna()

# Normalize
scaler = MinMaxScaler()
scaled_close = scaler.fit_transform(df)

# Generate sequences
def create_sequences(data_array: np.ndarray, win_size: int) -> tuple[np.ndarray, np.ndarray]:
    inputs, targets = [], []
    for i in range(win_size, len(data_array)):
        inputs.append(data_array[int(i - win_size):int(i)])
        targets.append(data_array[int(i)])
    return np.array(inputs), np.array(targets)

window_size: int = 60
X_all, y_all = create_sequences(scaled_close, window_size)

# Train/test split
split_idx: int = int(0.8 * len(X_all))
X_train, X_test = X_all[:split_idx], X_all[split_idx:]
y_train, y_test = y_all[:split_idx], y_all[split_idx:]

# Reshape for LSTM
X_train = X_train.reshape((int(X_train.shape[0]), int(X_train.shape[1]), 1))
X_test = X_test.reshape((int(X_test.shape[0]), int(X_test.shape[1]), 1))

# --- LSTM Model ---
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(units=50),
    Dropout(0.2),
    Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# --- Predictions ---
y_pred_scaled = model.predict(X_test)
y_pred = scaler.inverse_transform(y_pred_scaled)
y_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

# --- Evaluation Metrics ---
rmse = np.sqrt(mean_squared_error(y_actual, y_pred))
mae = mean_absolute_error(y_actual, y_pred)
mape = np.mean(np.abs((y_actual - y_pred) / y_actual)) * 100

print(f"LSTM RMSE: {rmse:.2f}")
print(f"LSTM MAE: {mae:.2f}")
print(f"LSTM MAPE: {mape:.2f}%")

# Save metrics to a cumulative CSV
metrics_file = os.path.join(reports_path, "Forecasting_Model_Metrics.csv")
metrics_df = pd.DataFrame([{
    "Model": "LSTM",
    "RMSE": round(rmse, 4),
    "MAE": round(mae, 4),
    "MAPE": round(mape, 2)
}])

# Append or create
if os.path.exists(metrics_file):
    existing_df = pd.read_csv(metrics_file)
    existing_df = existing_df[existing_df["Model"] != "LSTM"]
    full_df = pd.concat([existing_df, metrics_df], ignore_index=True)
else:
    full_df = metrics_df

full_df.to_csv(metrics_file, index=False)

# --- Plot Forecast Results ---
plt.figure(figsize=(10, 5))
plt.plot(y_actual, label="Actual")
plt.plot(y_pred, label="LSTM Forecast", linestyle="--")
plt.title("LSTM Actual vs Forecast")
plt.legend()
plt.savefig(os.path.join(figs_path, "lstm_actual_vs_forecast.png"))
plt.close()

# --- Plot Training Loss ---
plt.figure(figsize=(10, 4))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("LSTM Training & Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.savefig(os.path.join(figs_path, "lstm_training_loss.png"))
plt.close()

# --- Save model ---
model.save(os.path.join(models_path, "lstm_model.h5"))     # legacy
model.save(os.path.join(models_path, "lstm_model.keras"))  # recommended

from tensorflow.keras.models import load_model

# Load the saved Keras model (if you want to reuse it)
model = load_model(os.path.join(models_path, "lstm_model.keras"))


