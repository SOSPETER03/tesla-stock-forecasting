
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.graphics.gofplots import qqplot

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
csv_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
reports_path = os.path.join(project_root, "results", "reports")
os.makedirs(figs_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)

df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')
df["Return"] = df["Close"].pct_change()
df["Return_lag1"] = df["Return"].shift(1)
df.dropna(inplace=True)
exog = df[["Volume", "Return_lag1"]]

model = SARIMAX(df["Close"], exog=exog, order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit(disp=False)
df["forecast"] = results.predict(start=0, end=len(df)-1, exog=exog)

rmse = np.sqrt(mean_squared_error(df["Close"], df["forecast"]))
mae = mean_absolute_error(df["Close"], df["forecast"])
mape = np.mean(np.abs((df["Close"] - df["forecast"]) / df["Close"])) * 100

metrics_file = os.path.join(reports_path, "Forecasting_Model_Metrics.csv")
entry = pd.DataFrame([{"Model": "SARIMAX", "RMSE": round(rmse, 4), "MAE": round(mae, 4), "MAPE": round(mape, 2)}])
if os.path.exists(metrics_file):
    current = pd.read_csv(metrics_file)
    current = current[current["Model"] != "SARIMAX"]
    pd.concat([current, entry], ignore_index=True).to_csv(metrics_file, index=False)
else:
    entry.to_csv(metrics_file, index=False)

plt.figure(figsize=(10, 5))
plt.plot(df["Close"], label="Actual")
plt.plot(df["forecast"], label="SARIMAX Forecast", linestyle="--")
plt.legend()
plt.title("SARIMAX Actual vs Forecast with Exogenous Variables")
plt.savefig(os.path.join(figs_path, "sarimax_actual_vs_forecast.png"))
plt.close()
