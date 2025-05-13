import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import STL

# Load cleaned data
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")

# Ensure output directory exists
fig_dir = os.path.join(project_root, "results", "figures")
os.makedirs(fig_dir, exist_ok=True)

# 1. Plot Closing Price
plt.figure(figsize=(12, 5))
df["Close"].plot(title="Tesla Closing Price Over Time")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_closing_price.png"))
plt.close()

# 2. Plot Returns
plt.figure(figsize=(12, 5))
df["return"].plot(title="Daily Return Over Time")
plt.ylabel("Return")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_returns.png"))
plt.close()

# 3. Plot Volatility (Rolling Std)
plt.figure(figsize=(12, 5))
df["rolling_std_20"].plot(title="20-Day Rolling Volatility")
plt.ylabel("Volatility")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_volatility.png"))
plt.close()

# 4. Boxplots for Return and Volume
plt.figure(figsize=(6, 4))
sns.boxplot(y=df["return"].dropna())
plt.title("Boxplot - Returns")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_boxplot_returns.png"))
plt.close()

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Volume"].dropna())
plt.title("Boxplot - Volume")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_boxplot_volume.png"))
plt.close()

# 5. Descriptive Statistics
desc_stats = df[["return", "log_return", "rolling_std_20", "Volume"]].describe().T
desc_stats["skew"] = df[desc_stats.index].skew()
desc_stats["kurtosis"] = df[desc_stats.index].kurtosis()
print("📊 Descriptive Statistics with Skewness and Kurtosis:")
print(desc_stats)

# 6. ACF & PACF of Returns
plot_acf(df["return"].dropna(), lags=30)
plt.title("ACF - Returns")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_acf_returns.png"))
plt.close()

plot_pacf(df["return"].dropna(), lags=30)
plt.title("PACF - Returns")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_pacf_returns.png"))
plt.close()

# 7. STL Decomposition (Additive)
stl = STL(df["Close"], period=365)  # for daily data with yearly seasonality
res = stl.fit()

res.trend.plot(title="STL Decomposition - Trend")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_stl_trend.png"))
plt.close()

res.seasonal.plot(title="STL Decomposition - Seasonal")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_stl_seasonal.png"))
plt.close()

res.resid.plot(title="STL Decomposition - Residual")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_stl_residual.png"))
plt.close()

# 8. Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df[["return", "log_return", "close_lag1", "rolling_mean_20", "rolling_std_20", "Volume"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "eda_corr_matrix.png"))
plt.close()
