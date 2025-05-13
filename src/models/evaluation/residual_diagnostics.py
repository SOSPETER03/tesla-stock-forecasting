import os
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import acf

# --- Paths ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
data_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
reports_path = os.path.join(project_root, "results", "reports")
os.makedirs(reports_path, exist_ok=True)

# --- Load Data ---
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
df = df[["Close"]].dropna()

# --- Define Models ---
models = {
    "ARIMA": SARIMAX(df["Close"], order=(1, 1, 1)),
    "SARIMA": SARIMAX(df["Close"], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)),
    "SARIMAX": SARIMAX(df["Close"], exog=df["Close"].shift(1).fillna(method='bfill'), order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)),
}

# --- Evaluate Residuals ---
results = []
for name, model in models.items():
    fit = model.fit(disp=False)
    resid = fit.resid.dropna()

    # Ljung-Box test at lag 10
    ljungbox = acorr_ljungbox(resid, lags=[10], return_df=True)
    lb_pval = ljungbox["lb_pvalue"].iloc[0]

    # ACF at lags 1–3
    acf_vals = acf(resid, fft=False, nlags=10)
    results.append({
        "Model": name,
        "LjungBox_pval (lag 10)": round(lb_pval, 4),
        "ACF(lag 1)": round(acf_vals[1], 4),
        "ACF(lag 2)": round(acf_vals[2], 4),
        "ACF(lag 3)": round(acf_vals[3], 4),
    })

# --- Save Output ---
df_results = pd.DataFrame(results)
output_path = os.path.join(reports_path, "residual_diagnostics.csv")
df_results.to_csv(output_path, index=False)
print(f"Residual diagnostics saved to: {output_path}")
print(df_results)
