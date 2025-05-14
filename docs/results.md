#  Results and Model Evaluation

This section presents the evaluation of all models used in the project using key performance metrics visual forecasts and residual analysis

---

## AR Model Evaluation

- Metrics MAE MSE RMSE MAPE
- Plot figuresar_actual_vs_forecastpng

---

## MA Model Evaluation

- Metrics MAE MSE RMSE MAPE
- Plot figuresma_actual_vs_forecastpng

---

## ARIMA Model Evaluation

- Metrics MAE MSE RMSE MAPE AIC BIC
- Plot figuresarima_actual_vs_forecastpng

---

## SARIMA Model Evaluation

- Metrics MAE MSE RMSE MAPE AIC BIC
- Plots figuressarima_actual_vs_forecastpng

---

## SARIMAX Model Evaluation

- Metrics MAE MSE RMSE MAPE AIC BIC
- Plots
  - Forecast figuressarimax_actual_vs_forecastpng
  - ACF figuressarimax_residual_acfpng
  - PACF figuressarimax_residual_pacfpng
  - QQ figuressarimax_qq_plotpng

---

## STL Decomposition for Seasonal Structure

- Plots
  - STL Trend figureseda_stl_trendpng
  - STL Seasonal figureseda_stl_seasonalpng

---

## LSTM Model Evaluation

- Metrics MAE RMSE MAPE
- Plots
  - Forecast vs Actual figureslstm_actual_vs_forecastpng
  - Training Loss figureslstm_training_losspng

---

## Hybrid ARIMA  LSTM

- Plot figureshybrid_arima_lstm_forecastpng

---

## Boxplots of Errors

- Returns figuresreturn_boxplotpng
- Volume figuresVolume_boxplotpng