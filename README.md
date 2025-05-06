<<<<<<< HEAD
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
=======
# Advanced Time Series Forecasting of Tesla Stock
Comparative Analysis of Classical, Seasonal, and Deep Learning Models with Exogenous Predictors

🧠 ARIMA, Seasonal Decomposition, and Neural Networks for Enhanced Stock Price Prediction

## Overview
This project presents a comprehensive time series analysis and forecasting framework for Tesla Inc. stock prices using a diverse suite of models:
- Classical statistical models (AR, MA, ARIMA)
- Seasonal models (SARIMA, Seasonal Decomposition)
- Deep learning approaches (LSTM Neural Networks)
- Exogenous variable-enhanced models (ARIMAX, SARIMAX)
- Hybrid methodologies (combining statistical + machine learning)

## Project Details
- Data Source: Yahoo Finance via yfinance
- Stock Ticker: TSLA (Tesla Inc.)
- Time Period: January 2015 – January 2024
- Programming Language: Python
- Project Type: Time Series Forecasting & Predictive Modeling

## Tools & Libraries
- pandas, numpy – Data wrangling and preprocessing
- matplotlib, seaborn, plotly – Visualization
- statsmodels, pmdarima – Classical & Seasonal time series models
- tensorflow, keras – Deep learning (LSTM)
- scikit-learn – Evaluation and scaling
- yfinance – Stock data extraction

## Objectives
- Perform exploratory data analysis (EDA) on Tesla's historical stock prices and returns
- Build and compare AR, MA, ARIMA, and SARIMA models
- Implement exogenous variable models (e.g., ARIMAX, SARIMAX)
- Train and evaluate deep learning models such as LSTM for sequence prediction
- Compare classical vs deep learning approaches
- Evaluate model performance using:
  - RMSE, MAE, MAPE
  - AIC / BIC
  - Ljung-Box test (residual independence)
  - Residual plots and prediction accuracy

## Model Suite
- AR, MA, ARIMA: Classical univariate models for time series
- SARIMA: Seasonal modeling with trend + seasonality
- ARIMAX / SARIMAX: Includes external regressors
- Seasonal Decomposition: Trend, Seasonality, Residual breakdown
- LSTM (RNN): Deep learning for sequential data
- Hybrid Models: Combinations (e.g., ARIMA + LSTM)

## Results Summary
✅ Best Classical Model: SARIMA(1,1,1)(1,1,0)[12]
✅ Best Deep Learning Model: LSTM with TimeDistributed layers
✅ Hybrid models performed competitively, combining low bias and high sequence learning

## Key Insights
- Seasonality and external market signals improved accuracy
- Deep learning models showed strong performance on volatile periods
- Hybrid strategies delivered the most consistent forecasts in noisy datasets

## Project Structure
```markdown
>>>>>>> 90b4c53e9b6fcdd422dcbe20f428bf393761be38
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

<<<<<<< HEAD
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
=======
## Future Work
- Integrate Prophet by Meta for trend + seasonality forecasting
- Include macroeconomic exogenous
>>>>>>> 90b4c53e9b6fcdd422dcbe20f428bf393761be38
