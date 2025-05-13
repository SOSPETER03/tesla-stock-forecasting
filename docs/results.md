## 📦 Outlier Detection Boxplots

The following boxplots help visualize potential outliers in Tesla stock data:

### 🔹 Return Distribution
![Return Boxplot](../results/figures/return_boxplot.png)

This boxplot visualizes the daily return distribution of Tesla stock.  
Most returns cluster tightly around zero, indicating overall price stability on a day-to-day basis.  
However, there are several significant outliers both above and below, representing days of unusual gains or losses, likely due to earnings announcements or market shocks.

### 🔹 Volume Distribution
![Volume Boxplot](../results/figures/Volume_boxplot.png)

The boxplot for trading volume shows a wide range with a heavy upper tail.  
This indicates that while most days have moderate trading activity, there are several high-volume outliers, which may coincide with news events, quarterly earnings releases, or broader market moves.  
Such spikes in volume often reflect investor reactions to new information or speculation.


### ARIMA Model Evaluation Summary

We fit an ARIMA(1,1,1) model to Tesla's closing stock prices. Key evaluation metrics:

- AIC: 14,763.84
- BIC: 14,781.14
- Log Likelihood: -7,378.92
- RMSE: ~5.53 (computed from predictions)
- Residual Diagnostics:
  - Ljung-Box Q (lag 1): 0.43 (p ≈ 0.51) → residuals uncorrelated
  - Jarque-Bera: 15,947.58 (p < 0.001) → residuals not normally distributed
  - Heteroskedasticity: Strong presence (H = 539.95)
  - Skewness: -0.10
  - Kurtosis: 15.74 (leptokurtic)

Overall, ARIMA(1,1,1) captures short-term dynamics but residuals indicate volatility clustering and heavy tails. Suitable for baseline forecasting.
---

## 🔁 STL Decomposition for Seasonal Structure

We performed Seasonal-Trend Decomposition using Loess (STL) to separate the Tesla closing price into trend, seasonal, and residual components.

### 🔹 Trend Component
![STL Trend](../results/figures/eda_stl_trend.png)  
The trend captures the long-term upward trajectory of Tesla stock, showing acceleration during 2020–2021 and some plateauing post-2022.

### 🔹 Seasonal Component
![STL Seasonal](../results/figures/eda_stl_seasonal.png)  
The seasonal component reveals mild recurring monthly fluctuations, suggesting a 12-period seasonality — validating the use of SARIMA’s seasonal order `(P,D,Q,12)`.

**Interpretation**:  
The presence of clear seasonal patterns and long-term trend justifies SARIMA over standard ARIMA. Residuals from STL showed no strong periodicity beyond this.

---

## 📈 SARIMA Model Evaluation Summary
---

## 🧠 Seasonal Decomposition Analysis

To better inform seasonal model configurations, we applied both **STL decomposition** and **classical seasonal decomposition** on Tesla’s closing price.

### 📊 STL Decomposition (Seasonal-Trend using Loess)

![STL Decomposition](../results/figures/stl_decomposition.png)

**Interpretation**:  
- **Trend**: Shows strong upward movement, especially during 2020–2021.  
- **Seasonal**: Regular, mild repeating cycles validate using **SARIMA(·,·,·)(·,·,·,12)**.  
- **Residuals**: No clear leftover structure, indicating good seasonal capture.

### 📊 Classical Decomposition

![Classical Decomposition](../results/figures/classical_decomposition.png)

**Interpretation**:  
- Reinforces STL insights.  
- Slightly less smooth components than STL.  
- Confirms stable 12-month seasonality, supporting SARIMA’s seasonal configuration.
