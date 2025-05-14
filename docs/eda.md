#  Exploratory Data Analysis EDA

This section presents visual and statistical analysis of Teslas historical stock behavior to inform model development

---

## 1  Tesla Closing Price Over Time
Closing Pricefigureseda_closing_pricepng  
Interpretation Teslas stock price exhibits exponential growth from late 2019 to 2022 followed by high volatility This trend reflects investor enthusiasm and market dynamics

---

## 2  Daily Returns Over Time
Returnsfigureseda_returnspng  
Interpretation Returns are centered around zero with spikes during major events eg 2020 pandemic Modeling returns captures short-term fluctuations and risk

---

## 3  20-Day Rolling Volatility
Volatilityfigureseda_volatilitypng  
Interpretation Volatility surged during 2020 and 2022 aligning with market uncertainty Rolling volatility helps evaluate changing risk

---

## 4  Outlier Detection via Boxplots

Returns  
Return Boxplotfigureseda_boxplot_returnspng  

Volume  
Volume Boxplotfigureseda_boxplot_volumepng  

Interpretation Outliers in returns and volume highlight extreme events These may influence model sensitivity and require preprocessing

---

## 5  Descriptive Statistics

 Feature            Mean        Skewness  Kurtosis 
--------------------------------------------------
 Return             00018      0179     434     
 Log Return         00012      -0159    452     
 Rolling Std 20   673        169      294     
 Volume             114e08    274      1333    

Interpretation Non-normal behavior in volume high kurtosis skewness suggests episodic surges in trading activity



## 6  Correlation Matrix
Correlation Matrixfigureseda_corr_matrixpng  
Interpretation Strong correlation between lag and rolling features confirms temporal structure Weak correlation between volume and return aligns with financial theory

---

## 7  ACF and PACF of Returns

ACF  
ACFfigureseda_acf_returnspng  

PACF  
PACFfigureseda_pacf_returnspng  

Interpretation Lag 1 exhibits weak autocorrelation Higher-order lags contribute little supporting simpler ARMA models

---

## 8  STL Decomposition

Trend  
Trendfigureseda_stl_trendpng  

Seasonal  
Seasonalfigureseda_stl_seasonalpng  

Residual  
Residualfigureseda_stl_residualpng  

Interpretation A strong upward trend and mild seasonality are present Residuals highlight irregular fluctuations for model calibration

---
