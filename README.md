# 📈 Advanced Time Series Forecasting of Tesla Stock
**Comparative Analysis of Classical, Seasonal, and Deep Learning Models with Exogenous Predictors**

---

## 🧠 Overview
This project presents a comprehensive time series forecasting framework for Tesla Inc. (TSLA) stock using a range of modeling techniques:

- 📊 Classical statistical models: AR, MA, ARIMA  
- 📅 Seasonal models: SARIMA, Seasonal Decomposition  
- 🤖 Deep learning: LSTM Neural Networks  
- 📈 Exogenous variable-enhanced models: ARIMAX, SARIMAX  
- 🧬 Hybrid methodologies: Statistical + Machine Learning combinations  

---

## 📌 Project Details
- **Data Source:** Yahoo Finance (`yfinance`)
- **Ticker:** TSLA
- **Time Frame:** January 2015 – January 2024
- **Language:** Python
- **Type:** Time Series Forecasting & Predictive Modeling

---

## 🛠️ Tools & Libraries
- `pandas`, `numpy` – Data wrangling and preprocessing  
- `matplotlib`, `seaborn`, `plotly` – Visualization  
- `statsmodels`, `pmdarima` – Classical & Seasonal time series models  
- `tensorflow`, `keras` – Deep learning (LSTM)  
- `scikit-learn` – Evaluation and scaling  
- `yfinance` – Stock data extraction  

---

## 🎯 Objectives
- Perform EDA on Tesla’s historical stock prices & returns  
- Build and compare AR, MA, ARIMA, and SARIMA models  
- Implement exogenous variable models (e.g., ARIMAX, SARIMAX)  
- Train and evaluate deep learning models such as LSTM for sequence prediction  
- Compare classical vs deep learning approaches  
- Evaluate model performance using:
  - RMSE, MAE, MAPE
  - AIC / BIC
  - Ljung-Box test for residual independence  
  - Residual plots and prediction accuracy

---

## 🔍 Model Suite
- **AR, MA, ARIMA:** Classical univariate models for time series  
- **SARIMA:** Seasonal modeling with trend + seasonality  
- **ARIMAX / SARIMAX:** Includes external regressors  
- **Seasonal Decomposition:** Trend, Seasonality, Residual breakdown  
- **LSTM (RNN):** Deep learning for sequential data  
- **Hybrid Models:** Combinations (e.g., ARIMA + LSTM)

---

## ✅ Results Summary
- **Best Classical Model:** `SARIMA(1,1,1)(1,1,0)[12]`  
- **Best Deep Learning Model:** LSTM with TimeDistributed layers  
- **Best Hybrid:** ARIMA + LSTM performed competitively  

**Key Insights:**
- Seasonality and external market signals improved accuracy  
- Deep learning models showed strong performance on volatile periods  
- Hybrid strategies delivered the most consistent forecasts in noisy datasets  

---

## 📁 Project Structure
```
tesla-stock-forecasting/
├── data/
│   └── raw/
├── src/
│   ├── models/
│   │   ├── classical/
│   │   └── deep_learning/
│   ├── preprocessing/
│   └── visualization/
├── notebooks/
└── results/
```

---

## 🔮 Future Work
- Integrate **Meta Prophet** for trend + seasonality forecasting  
- Include macroeconomic indicators as exogenous variables  
- Deploy a web dashboard for interactive forecast visualization  

---

## 📬 Contact
**Sospeter Njenga Wainaina**  
📧 sospeternjenga03@gmail.com  
📍 Nairobi, Kenya



## 🔟 Conclusion & Recommendations

### ✅ **Best Performing Model**
After evaluating six models — **AR, MA, ARIMA, SARIMA, SARIMAX, and LSTM**, and implementing a **Hybrid ARIMA + LSTM**, we conclude:

> 🔥 **Hybrid ARIMA + LSTM** is the most accurate model for forecasting Tesla stock prices.

- It outperformed others in **RMSE, MAE, MAPE**.
- Statistically significant accuracy advantage confirmed via **Diebold-Mariano test** vs. SARIMAX (`p ≈ 0.0000`).

---

### 🧠 **Model Strengths by Category**

| Model       | Strengths                                                                 | Best Use Cases                                     |
|-------------|---------------------------------------------------------------------------|---------------------------------------------------|
| **AR / MA** | Simplicity, fast computation                                              | Short-term trend capturing, quick benchmarks      |
| **ARIMA**   | Handles non-stationarity                                                  | Medium-term forecasting without seasonality       |
| **SARIMA**  | Accounts for both trend + seasonality                                     | Monthly/quarterly financial patterns              |
| **SARIMAX** | Integrates external variables like volume or lagged returns               | Multivariate forecasting, macro-driven influence  |
| **LSTM**    | Learns complex, nonlinear temporal dependencies                           | High-volatility prediction, adaptive learning     |
| **Hybrid**  | ARIMA models trend, LSTM models residuals (nonlinear patterns)            | **Highly volatile, non-linear series like stocks**|

---

### ⚠️ **Limitations**
- **No macroeconomic data** like interest rates or inflation included.
- **LSTM training** can be time-consuming and sensitive to hyperparameters.
- **Assumes stable market conditions**, which may not hold in extreme economic events.

---

### 🚀 **Future Improvements**
- Add **exogenous features** (e.g., S&P500 index, news sentiment, global indicators).
- Tune deep learning models with **Bayesian optimization** or **Grid Search**.
- Explore **attention-based architectures** like Transformer models for enhanced context learning.
- Deploy as a **web app using Streamlit** for interactive forecasting.
