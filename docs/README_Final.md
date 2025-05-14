
# 📈 Tesla Stock Forecasting: Comparative Modeling Project

A complete end-to-end time series forecasting project predicting **Tesla (TSLA)** stock prices using classical statistical models and deep learning approaches. This project implements, compares, and evaluates models including AR, MA, ARIMA, SARIMA, SARIMAX, LSTM, and a hybrid ARIMA+LSTM model.

---

## 🧠 Models Implemented

| Model        | Type           | Seasonality | Exogenous | Deep Learning | Hybrid | Evaluation |
|--------------|----------------|-------------|-----------|----------------|--------|------------|
| AR, MA       | Classical       | ❌           | ❌         | ❌              | ❌      | ✅          |
| ARIMA        | Classical       | ❌           | ❌         | ❌              | ❌      | ✅          |
| SARIMA       | Classical       | ✅           | ❌         | ❌              | ❌      | ✅          |
| SARIMAX      | Classical       | ✅           | ✅         | ❌              | ❌      | ✅          |
| LSTM         | Deep Learning   | ❌           | ✅         | ✅              | ❌      | ✅          |
| ARIMA + LSTM | Hybrid          | Partial      | ✅         | ✅              | ✅      | ✅          |

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas, NumPy, Matplotlib, Seaborn
- `statsmodels`, `pmdarima`
- Scikit-learn
- TensorFlow / Keras
- yfinance (data fetching)
- Streamlit (optional dashboard)

---

## 📂 Project Structure

```
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── classical_models.ipynb
├── src/
│   ├── preprocessing/
│   ├── models/
│   ├── evaluation/
│   ├── visualization/
│   └── deep_learning/
├── results/
│   ├── figures/
│   ├── models/
│   └── reports/
├── results.md
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/SOSPETER03/tesla-stock-forecasting.git
cd tesla-stock-forecasting
```

### 2. Setup virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run notebooks or scripts

```bash
jupyter notebook  # explore classical_models.ipynb
```

---

## 📊 Results Snapshot

- Best Classical Model: **SARIMAX**
- Best Overall: **Hybrid ARIMA + LSTM**
- Evaluation metrics: RMSE, MAE, MAPE
- Residual diagnostics: ACF, Ljung-Box test
- Comparison: All models visualized and benchmarked

---

## 📌 Project Highlights

- 📉 Time Series Stationarity checks (ADF, KPSS)
- 🔁 Model tuning via AIC/BIC and grid search
- 🧮 Statistical diagnostics on residuals
- 📚 Modular Python scripts for reusability
- 🧠 Deep Learning sequence modeling
- 📈 Hybrid ensemble forecasting

---

## 👤 Author

**Sospeter Njenga Wainaina**  
- [GitHub Profile](https://github.com/SOSPETER03)
- [LinkedIn](https://linkedin.com) *(add your link)*

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---
