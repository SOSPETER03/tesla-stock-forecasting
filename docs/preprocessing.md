
# 🧼 Preprocessing Summary

## ✔️ Initial Data Checks
- **Rows & Columns:** 2,274 rows × 5 columns
- **Date Range:** 2015-01-02 to 2024-01-16
- **Data Types:**
  - Open, High, Low, Close → float64
  - Volume → int64
- **Datetime Index Set:** Yes
- **Frequency Check:** Could not be inferred (irregular calendar days)

## 🛠 Feature Engineering
- `return`: Daily percentage change of the closing price
- `log_return`: Natural log of (1 + return)
- `close_lag1`: Previous day's closing price
- `rolling_mean_20`: 20-day moving average of Close
- `rolling_std_20`: 20-day rolling standard deviation (volatility)

## 📦 Outlier Detection
- **Return Outliers:** 143 (via IQR method and boxplot)
- **Volume Outliers:** 162 (indicative of major trading events or anomalies)

## 🔎 Stationarity Testing
- **ADF Test (Close):** p = 0.6687 → Non-stationary
- **KPSS Test (Close):** p = 0.0100 → Trend non-stationary
- **Differencing Applied:** 1st order (`d = 1`)
- ✅ **Stationarity achieved after differencing**
