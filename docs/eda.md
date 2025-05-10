# 📊 Exploratory Data Analysis (EDA)

## 1. Tesla Closing Price Over Time
![Closing Price](../results/figures/eda_closing_price.png)  
Interpretation: The Tesla stock price shows exponential growth from late 2019 to 2022, followed by high volatility. The upward trend indicates strong momentum, while frequent sharp movements suggest active market behavior.

## 2. Daily Returns Over Time
![Returns](../results/figures/eda_returns.png)  
Interpretation: Returns fluctuate tightly around zero, with noticeable spikes during volatile market periods (e.g., 2020 pandemic). This supports further modeling of return dynamics.

## 3. 20-Day Rolling Volatility
![Volatility](../results/figures/eda_volatility.png)  
Interpretation: Volatility spiked significantly during early 2020 and early 2022, indicating market uncertainty. Rolling volatility helps assess risk across different periods.

## 4. Boxplots for Outlier Detection

Returns:  
![Return Boxplot](../results/figures/eda_boxplot_returns.png)  

Volume:  
![Volume Boxplot](../results/figures/eda_boxplot_volume.png)  

Interpretation: Both returns and volume display substantial outliers. These extreme values should be carefully handled in model building to avoid distortion.

## 5. Descriptive Statistics

| Feature | Mean | Skewness | Kurtosis |
|------- |------|----------|----------|
| Return | ~0.0018 | 0.179 | 4.34 |
| Log Return | ~0.0012 | -0.159 | 4.52 |
| Rolling Std (20) | ~6.73 | 1.69 | 2.94 |
| Volume | ~1.14e+08 | 2.74 | 13.33 |

Interpretation: High kurtosis and skewness in volume indicate heavy tails and asymmetry, implying non-normal behavior.

## 6. Correlation Matrix
![Correlation Matrix](../results/figures/eda_corr_matrix.png)  
Interpretation: High correlation between `close_lag1` and `rolling_mean_20` suggests redundancy. Volume has weak correlation with returns but can be informative when modeling volatility.

## 7. Autocorrelation and Partial Autocorrelation

ACF - Returns:  
![ACF](../results/figures/eda_acf_returns.png)  

PACF - Returns:  
![PACF](../results/figures/eda_pacf_returns.png)  

Interpretation: Minimal autocorrelation beyond lag 1 suggests weak temporal dependency, a key observation for ARMA/ARIMA modeling.

## 8. STL Decomposition

Trend:  
![Trend](../results/figures/eda_stl_trend.png)  

Seasonal:  
![Seasonal](../results/figures/eda_stl_seasonal.png)  

Residual:  
![Residual](../results/figures/eda_stl_residual.png)  

Interpretation: STL decomposition uncovers a strong upward trend and changing seasonal patterns. The residuals contain noise and abrupt shifts—ideal for evaluating stationarity and model fitting.
