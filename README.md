# 📈 Advanced Time Series Forecasting of Tesla Stock

**Comparative Analysis of Classical, Seasonal, and Deep Learning Models with Exogenous Predictors**

---

## 🧠 Overview

This project presents a comprehensive time series forecasting framework for **Tesla Inc. (TSLA)** stock using a range of modeling techniques:

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

- `pandas`, `numpy` – Data handling and preprocessing  
- `matplotlib`, `seaborn`, `plotly` – Visualization  
- `statsmodels`, `pmdarima` – Classical & seasonal modeling  
- `tensorflow`, `keras` – Deep learning (LSTM)  
- `scikit-learn` – Evaluation, scaling  
- `yfinance` – Stock data extraction  

---

## 🎯 Objectives

- Perform EDA on Tesla’s historical prices & returns  
- Develop & compare AR, MA, ARIMA, and SARIMA models  
- Implement models with exogenous variables (ARIMAX, SARIMAX)  
- Train deep learning models (LSTM) for sequence prediction  
- Evaluate performance using metrics:
  - RMSE, MAE, MAPE
  - AIC / BIC
  - Ljung-Box test for residual independence  
  - Residual diagnostics & visual prediction accuracy  

---

## 🔍 Model Suite

- **AR, MA, ARIMA:** Univariate classical models  
- **SARIMA:** Seasonal model with trend/seasonality  
- **ARIMAX / SARIMAX:** Multivariate with external regressors  
- **Seasonal Decomposition:** Trend, seasonality, residuals  
- **LSTM (RNN):** Deep learning for sequential modeling  
- **Hybrid Models:** e.g., ARIMA + LSTM

---

## ✅ Results Summary

- **Best Classical Model:** `SARIMA(1,1,1)(1,1,0)[12]`  
- **Best Deep Learning Model:** LSTM with `TimeDistributed` layers  
- **Best Hybrid:** ARIMA + LSTM performed competitively  
- **Insights:**
  - Seasonality & exogenous variables boost accuracy  
  - LSTM excels in volatile/irregular periods  
  - Hybrid models yield stable forecasts in noisy data  

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
- Add macroeconomic indicators as exogenous variables  
- Deploy a web dashboard for interactive forecast visualization  

---

## 📬 Contact

Sospeter Njenga Wainaina  
📧 sospeternjenga03@gmail.com  
📍 Nairobi, Kenya  
