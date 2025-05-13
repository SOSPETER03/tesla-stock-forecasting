import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

# --- Set paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
csv_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
os.makedirs(figs_path, exist_ok=True)

# --- Load data
df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')

# --- Seasonal differencing (assume seasonality = 12 for monthly-like seasonality)
seasonal_diff = df["Close"].diff(12).dropna()

# --- ADF Test
adf_result = adfuller(seasonal_diff)
print(f"ADF Statistic: {adf_result[0]:.2f}")
print(f"p-value: {adf_result[1]:.4f}")

# --- ACF and PACF Plots
plt.figure()
plot_acf(seasonal_diff, lags=40)
plt.title("ACF after Seasonal Differencing")
plt.savefig(os.path.join(figs_path, "sarima_acf_seasonal_diff.png"))
plt.close()

plt.figure()
plot_pacf(seasonal_diff, lags=40)
plt.title("PACF after Seasonal Differencing")
plt.savefig(os.path.join(figs_path, "sarima_pacf_seasonal_diff.png"))
plt.close()

# --- Fit SARIMA Model
model = SARIMAX(df["Close"], order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit(disp=False)

# --- Print summary
print(results.summary())

# --- Forecast vs Actual Plot
forecast = results.predict(start=0, end=len(df)-1)
plt.figure(figsize=(10,5))
plt.plot(df["Close"], label="Actual")
plt.plot(forecast, label="SARIMA Forecast", linestyle="--")
plt.title("SARIMA Actual vs Forecast")
plt.legend()
plt.savefig(os.path.join(figs_path, "sarima_actual_vs_forecast.png"))
plt.close()
