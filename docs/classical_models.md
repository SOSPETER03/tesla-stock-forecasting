python
import pandas as pd
import numpy as np
import matplotlibpyplot as plt
import seaborn as sns
from statsmodelstsaarimamodel import ARIMA
from statsmodelsgraphicstsaplots import plot_acf plot_pacf
from statsmodelsstatsdiagnostic import acorr_ljungbox
from sklearnmetrics import mean_squared_error mean_absolute_error
import os

# Load cleaned data
data_path  dataprocessedTesla_Cleanedcsv
df  pdread_csvdata_path parse_datesDate index_colDate
df  dfasfreqB  # business day frequency
dfClose  dfCloseinterpolate





python
plot_acfdfClosedropna lags40
plttitleACF of Close Prices
pltshow

plot_pacfdfClosedropna lags40
plttitlePACF of Close Prices
pltshow




    
pngclassical_models_filesclassical_models_1_0png
    



    
pngclassical_models_filesclassical_models_1_1png
    



python
# Fit ARIMA model  example with 111
model  ARIMAdfClose order111
results  modelfit
printresultssummary



    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsastatespacesarimaxpy966 UserWarning Non-stationary starting autoregressive parameters found Using zeros as starting parameters
      warnNon-stationary starting autoregressive parameters
    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsastatespacesarimaxpy978 UserWarning Non-invertible starting MA parameters found Using zeros as starting parameters
      warnNon-invertible starting MA parameters found
    

                                   SARIMAX Results                                
    
    Dep Variable                  Close   No Observations                 2358
    Model                 ARIMA1 1 1   Log Likelihood               -7378920
    Date                Wed 07 May 2025   AIC                          14763839
    Time                        084913   BIC                          14781135
    Sample                    01-02-2015   HQIC                         14770137
                             - 01-16-2024                                         
    Covariance Type                  opg                                         
    
                     coef    std err          z      Pz      0025      0975
    ------------------------------------------------------------------------------
    arL1         -07061      0149     -4726      0000      -0999      -0413
    maL1          06789      0155      4369      0000       0374       0983
    sigma2        306735      0330     92939      0000      30027      31320
    
    Ljung-Box L1 Q                   043   Jarque-Bera JB             1594758
    ProbQ                              051   ProbJB                         000
    Heteroskedasticity H             53995   Skew                            -010
    ProbH two-sided                  000   Kurtosis                        1574
    
    
    Warnings
    1 Covariance matrix calculated using the outer product of gradients complex-step
    


python
residuals  resultsresid
pltfigurefigsize10 4
pltsubplot121
plot_acfresidualsdropna lags40
plttitleACF of Residuals

pltsubplot122
snshistplotresiduals kdeTrue
plttitleResidual Distribution
plttight_layout
pltshow

# Ljung-Box test
lb_test  acorr_ljungboxresiduals lags10 return_dfTrue
printLjung-Box Testn lb_test




    
pngclassical_models_filesclassical_models_3_0png
    



    
pngclassical_models_filesclassical_models_3_1png
    


    Ljung-Box Test
           lb_stat  lb_pvalue
    10  46134845   0000001
    


python
dfforecast  resultspredictstart0 endlendf-1
rmse  npsqrtmean_squared_errordfClose dfforecast
mae  mean_absolute_errordfClose dfforecast
mape  npmeannpabsdfClose - dfforecast  dfClose  100

printfRMSE rmse4f MAE mae4f MAPE mape2f

dfClose forecastplotfigsize125 titleARIMA Forecast vs Actual
pltshow



    RMSE 55454 MAE 27561 MAPE 242
    


    
pngclassical_models_filesclassical_models_4_1png
    



python
import pandas as pd
from statsmodelstsaarimamodel import ARIMA
import matplotlibpyplot as plt
from statsmodelsgraphicstsaplots import plot_acf
import os

# Load the cleaned dataset using the absolute path
df  pdread_csv
    CUserssospeterPycharmProjectspythonProjecttesla-stock-forecastingdataprocessedTesla_Cleanedcsv
    parse_datesDate
    index_colDate


# Fit ARIMA111
model  ARIMAdfClose order1 1 1
results  modelfit

# Extract residuals
residuals  resultsresid

# Save ACF plot of residuals
fig  plot_acfresiduals
osmakedirsresultsfigures exist_okTrue
figsavefigresultsfiguresarima_residual_acfpng
pltclose

print Residual ACF plot saved



    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    

     Residual ACF plot saved
    


python
import pandas as pd
import matplotlibpyplot as plt
from statsmodelstsaarimamodel import ARIMA
import os

# Load the cleaned dataset
df  pdread_csvrCUserssospeterPycharmProjectspythonProjecttesla-stock-forecastingdataprocessedTesla_Cleanedcsv 
                 parse_datesDate index_colDate



# Fit ARIMA111 model
model  ARIMAdfClose order1 1 1
results  modelfit

# Generate in-sample predictions same length as data
dfpredicted  resultspredictstart1 endlendf-1 dynamicFalse

# Plot Actual vs Predicted
pltfigurefigsize10 5
pltplotdfClose labelActual linewidth2
pltplotdfpredicted labelPredicted linewidth2 linestyle--
plttitleActual vs Predicted Closing Prices ARIMA Model
pltxlabelDate
pltylabelPrice
pltlegend

# Ensure the save directory exists
fig_path  resultsfigures
osmakedirsfig_path exist_okTrue
pltsavefigospathjoinfig_path arima_actual_vs_predictedpng
pltclose

print Actual vs Predicted plot saved to resultsfiguresarima_actual_vs_predictedpng



    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    CUserssospeterPycharmProjectspythonProjectvenv1Libsite-packagesstatsmodelstsabasetsa_modelpy473 ValueWarning A date index has been provided but it has no associated frequency information and so will be ignored when eg forecasting
      self_init_datesdates freq
    

     Actual vs Predicted plot saved to resultsfiguresarima_actual_vs_predictedpng
    


python


