
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error

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

# Fit ARIMA model
model = ARIMA(df["Close"], order=(1, 1, 1))
results = model.fit()

# Generate forecast
df["forecast"] = results.predict(start=0, end=len(df)-1)

# Drop NaNs from both columns for evaluation
eval_df = df[["Close", "forecast"]].dropna()

# Evaluation
rmse = np.sqrt(mean_squared_error(eval_df["Close"], eval_df["forecast"]))
mae = mean_absolute_error(eval_df["Close"], eval_df["forecast"])
mape = np.mean(np.abs((eval_df["Close"] - eval_df["forecast"]) / eval_df["Close"])) * 100

# Save metrics to CSV
metrics_file = os.path.join(reports_path, "Forecasting_Model_Metrics.csv")
metrics_row = pd.DataFrame([{
    "Model": "ARIMA",
    "RMSE": round(rmse, 4),
    "MAE": round(mae, 4),
    "MAPE": round(mape, 2)
}])
if os.path.exists(metrics_file):
    existing = pd.read_csv(metrics_file)
    existing = existing[existing["Model"] != "ARIMA"]
    updated = pd.concat([existing, metrics_row], ignore_index=True)
else:
    updated = metrics_row
updated.to_csv(metrics_file, index=False)

# Save plot
plt.figure(figsize=(10, 5))
plt.plot(df["Close"], label="Actual")
plt.plot(df["forecast"], label="ARIMA Forecast", linestyle="--")
plt.title("ARIMA Actual vs Forecast")
plt.legend()
plt.savefig(os.path.join(figs_path, "arima_actual_vs_forecast.png"))
plt.close()
