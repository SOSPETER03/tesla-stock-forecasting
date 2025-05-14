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
