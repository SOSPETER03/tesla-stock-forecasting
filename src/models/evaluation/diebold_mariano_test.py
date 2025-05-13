import os
import pandas as pd
from arch.__future__ import reindexing
from arch.bootstrap import optimal_block_length, StationaryBootstrap
from scipy import stats

# --- Paths ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
reports_path = os.path.join(project_root, "results", "reports")

# --- Load Actuals and Forecasts ---
sarimax_path = os.path.join(reports_path, "sarimax_forecast.csv")
hybrid_path = os.path.join(reports_path, "hybrid_forecast.csv")

sarimax_df = pd.read_csv(sarimax_path)
hybrid_df = pd.read_csv(hybrid_path)

# Assume both have 'Date', 'Actual', 'Forecast' columns
actual = sarimax_df["Actual"].values
e_sarimax = actual - sarimax_df["Forecast"].values
e_hybrid = actual - hybrid_df["Forecast"].values

# --- Loss differential ---
d = (e_sarimax ** 2) - (e_hybrid ** 2)

# --- Diebold-Mariano test ---
mean_d = d.mean()
var_d = d.var(ddof=1)
dm_stat = mean_d / (var_d / len(d)) ** 0.5
p_value = 2 * (1 - stats.norm.cdf(abs(dm_stat)))

print(f"Diebold-Mariano Test Statistic: {dm_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# --- Interpretation ---
if p_value < 0.05:
    print("✅ Statistically significant difference in forecast accuracy (reject H0).")
else:
    print("❌ No significant difference in forecast accuracy (fail to reject H0).")
