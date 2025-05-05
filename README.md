# 📈 Tesla Stock Forecasting Using AR, MA, and ARIMA Models

Predictive modeling for Tesla stock prices using AR, MA, and ARIMA models.  
A statistical and time-series analysis project using Python.

---

## 🧠 Overview

This project involves time series modeling and forecasting of Tesla Inc.'s stock prices using three classic statistical models:

- Autoregressive (AR)
- Moving Average (MA)
- Autoregressive Integrated Moving Average (ARIMA)

It provides a detailed analysis of stock return behavior, model performance diagnostics, and comparison to identify the most accurate forecasting technique.

---

## 📊 Project Details

- Data Source: Yahoo Finance (`yfinance`)
- Timeframe: Jan 2015 – Jan 2024
- Language: Python
- Tools Used: 
  - `pandas`, `numpy` for data manipulation  
  - `matplotlib`, `seaborn` for visualization  
  - `statsmodels` for time series modeling  
  - `yfinance` for stock data retrieval

---

## 🎯 Objectives

- Perform exploratory data analysis (EDA) on Tesla's historical daily returns.
- Implement and compare AR, MA, and ARIMA models.
- Evaluate performance using:
  - AIC (Akaike Information Criterion)
  - RMSE (Root Mean Square Error)
  - Ljung-Box test for residual diagnostics
- Forecast short-term stock returns and assess prediction accuracy.

---

## 🧪 Results Summary

- Best Model: ARIMA(1,1,1)
- Key Findings:
  - Lowest AIC and RMSE among all models
  - Residuals showed white noise behavior, validating model accuracy
  - ARIMA provided the most reliable short-term forecast

---

## 📁 Project Structure

```bash
tesla-stock-forecasting/
│
├── data/                   # Raw and processed data (optional to upload)
├── notebooks/              # Jupyter notebooks for modeling and analysis
├── report/                 # Final project report (PDF)
├── images/                 # Visualizations and charts (optional)
├── README.md               # Project description and guide
├── requirements.txt        # Project dependencies
└── .gitignore              # Files and folders to ignore in git
