import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.gofplots import qqplot
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# --- Set paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
csv_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
os.makedirs(figs_path, exist_ok=True)

# --- Load data
df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')
df["Return"] = df["Close"].pct_change()
df["Return_lag1"] = df["Return"].shift(1)
df.dropna(inplace=True)

# --- ADF test
seasonal_diff = df["Close"].diff(12).dropna()
adf_result = adfuller(seasonal_diff)
print(f"ADF Statistic (seasonal diff): {adf_result[0]:.2f}")
print(f"p-value: {adf_result[1]:.4f}")

# --- ACF and PACF plots
plot_acf(seasonal_diff, lags=40)
plt.title("SARIMAX ACF after Seasonal Differencing")
plt.savefig(os.path.join(figs_path, "sarimax_acf_seasonal_diff.png"))
plt.close()

plot_pacf(seasonal_diff, lags=40)
plt.title("SARIMAX PACF after Seasonal Differencing")
plt.savefig(os.path.join(figs_path, "sarimax_pacf_seasonal_diff.png"))
plt.close()

# --- Exogenous features
exog = df[["Volume", "Return_lag1"]]

# --- SARIMAX model
model_exog = SARIMAX(df["Close"], exog=exog, order=(1,1,1), seasonal_order=(1,1,1,12))
results_exog = model_exog.fit(disp=False)
print(results_exog.summary())

# --- Forecast
forecast_exog = results_exog.predict(start=0, end=len(df)-1, exog=exog)

# --- Evaluation Metrics
rmse = np.sqrt(mean_squared_error(df["Close"], forecast_exog))
mae = mean_absolute_error(df["Close"], forecast_exog)
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")

# --- Plot actual vs. forecast
plt.figure(figsize=(10, 5))
plt.plot(df["Close"], label="Actual")
plt.plot(forecast_exog, label="SARIMAX Forecast", linestyle="--")
plt.title("SARIMAX Actual vs Forecast with Exogenous Variables")
plt.legend()
plt.savefig(os.path.join(figs_path, "sarimax_actual_vs_forecast.png"))
plt.close()

# --- Residual diagnostics
residuals = results_exog.resid

plot_acf(residuals.dropna(), lags=40)
plt.title("SARIMAX Residuals ACF")
plt.savefig(os.path.join(figs_path, "sarimax_residual_acf.png"))
plt.close()

plot_pacf(residuals.dropna(), lags=40)
plt.title("SARIMAX Residuals PACF")
plt.savefig(os.path.join(figs_path, "sarimax_residual_pacf.png"))
plt.close()

qqplot(residuals.dropna(), line='s')
plt.title("SARIMAX Residuals Q-Q Plot")
plt.savefig(os.path.join(figs_path, "sarimax_qq_plot.png"))
plt.close()
