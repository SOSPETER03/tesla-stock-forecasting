# 📈 Advanced Time Series Forecasting of Tesla Stock  
Comparative Analysis of Classical, Seasonal, and Deep Learning Models with Exogenous Predictors

### 🧠 ARIMA, Seasonal Decomposition, and Neural Networks for Enhanced Stock Price Prediction

---

## 🧠 Overview

This project presents a comprehensive time series analysis and forecasting framework for Tesla Inc. stock prices using a diverse suite of models:

- Classical statistical models (AR, MA, ARIMA)
- Seasonal models (SARIMA, Seasonal Decomposition)
- Deep learning approaches (LSTM Neural Networks)
- Exogenous variable-enhanced models (ARIMAX, SARIMAX)
- Hybrid methodologies (combining statistical + machine learning)

The aim is to identify the most effective forecasting approach by analyzing model performance, residual behavior, and predictive accuracy.

---

## 📊 Project Details

- Data Source: [Yahoo Finance](https://finance.yahoo.com/) via `yfinance`  
- Stock Ticker: TSLA (Tesla Inc.)  
- Time Period: January 2015 – January 2024  
- Programming Language: Python  
- Project Type: Time Series Forecasting & Predictive Modeling  

### 🛠️ Tools & Libraries
- `pandas`, `numpy` – Data wrangling and preprocessing  
- `matplotlib`, `seaborn`, `plotly` – Visualization  
- `statsmodels`, `pmdarima` – Classical & Seasonal time series models  
- `tensorflow`, `keras` – Deep learning (LSTM)  
- `scikit-learn` – Evaluation and scaling  
- `yfinance` – Stock data extraction  

---

## 🎯 Objectives

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

---

## 📈 Model Suite

| Model Type              | Description                                   |
|-------------------------|-----------------------------------------------|
| AR, MA, ARIMA           | Classical univariate models for time series   |
| SARIMA                  | Seasonal modeling with trend + seasonality    |
| ARIMAX / SARIMAX        | Includes external regressors                  |
| Seasonal Decomposition  | Trend, Seasonality, Residual breakdown        |
| LSTM (RNN)              | Deep learning for sequential data             |
| Hybrid Models           | Combinations (e.g., ARIMA + LSTM)             |

---

## 📊 Results Summary

- ✅ Best Classical Model: SARIMA(1,1,1)(1,1,0)[12]  
- ✅ Best Deep Learning Model: LSTM with TimeDistributed layers  
- ✅ Hybrid models performed competitively, combining low bias and high sequence learning

### 🔍 Key Insights:
- Seasonality and external market signals improved accuracy  
- Deep learning models showed strong performance on volatile periods  
- Hybrid strategies delivered the most consistent forecasts in noisy datasets  

---

## 📁 Project Structure



---

## 📌 Future Work

- Integrate Prophet by Meta for trend + seasonality forecasting  
- Include macroeconomic exogenous predictors (e.g., inflation rates, interest rates, oil prices, market indices)  
- Explore ensemble methods and tree-based models (e.g., XGBoost) for time series  
- Develop a hybrid ARIMA-LSTM or SARIMA-MLP model  
- Deploy via Streamlit or Flask for interactive forecasting and visualization  
- Automate model retraining using cron jobs or Apache Airflow for real-time applications  
- Extend the project to include portfolio risk modeling and volatility forecasting (e.g., GARCH)

---

## 📚 References

- Hyndman, R.J. & Athanasopoulos, G. – *Forecasting: Principles and Practice*  
- [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)  
- [Keras LSTM for Time Series Forecasting](https://keras.io/examples/timeseries/timeseries_weather_forecasting/)  
- [Yahoo Finance API - yfinance](https://pypi.org/project/yfinance/)  
- Brownlee, J. – Deep Learning for Time Series Forecasting (Machine Learning Mastery)  

---

## 🙌 Author

Sospeter Njenga Wainaina 
Data Analyst | Aspiring Quant | Time Series & Forecasting Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/sospeter-njenga-405442220)  
📧 [sospeternjenga03@gmail.com](mailto:sospeternjenga03@gmail.com)  
🌐 [GitHub: SOSPETER03](https://github.com/SOSPETER03)

---

