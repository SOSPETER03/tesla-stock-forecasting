import os
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# --- Paths ---
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
data_path = os.path.join(root, "data", "processed", "Tesla_Cleaned.csv")
output_path = os.path.join(root, "results", "reports", "sarimax_forecast.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# --- Load Data ---
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
df = df[["Close"]].dropna()
train_size = int(0.8 * len(df))
train, test = df.iloc[:train_size], df.iloc[train_size:]

# --- Fit SARIMAX ---
exog = train["Close"].shift(1).fillna(method="bfill")
model = SARIMAX(train["Close"], exog=exog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
fit = model.fit(disp=False)

# --- Forecast ---
exog_test = test["Close"].shift(1).fillna(method="bfill")
forecast = fit.forecast(steps=len(test), exog=exog_test)

# --- Save Output ---
result_df = pd.DataFrame({
    "Date": test.index,
    "Actual": test["Close"].values,
    "Forecast": forecast.values
})
result_df.to_csv(output_path, index=False)
print(f"SARIMAX forecast saved to: {output_path}")
