import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from statsmodels.tsa.stattools import adfuller, kpss
import warnings

warnings.filterwarnings("ignore")

def load_and_prepare_data():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    csv_path = os.path.join(project_root, "data", "raw", "Tesla_Stock_Updated_V2.csv")

    df = pd.read_csv(csv_path)

    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values("Date", inplace=True)
    df.set_index("Date", inplace=True)

    df.ffill(inplace=True)
    df.interpolate(inplace=True)

    print("✅ Data Shape:", df.shape)
    print("✅ Data Types:\n", df.dtypes)
    print("✅ Date Range:", df.index.min(), "to", df.index.max())
    print("✅ Frequency Check:", pd.infer_freq(df.index))

    df['return'] = df['Close'].pct_change()
    df['log_return'] = np.log1p(df['return'])
    df['close_lag1'] = df['Close'].shift(1)
    df['rolling_mean_20'] = df['Close'].rolling(window=20).mean()
    df['rolling_std_20'] = df['Close'].rolling(window=20).std()

    return df, project_root

def detect_outliers(df_local, column, project_root):
    figs_path = os.path.join(project_root, "results", "figures")
    os.makedirs(figs_path, exist_ok=True)

    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df_local[column])
    plt.title(f"Boxplot for {column}")
    plt.savefig(os.path.join(figs_path, f"{column}_boxplot.png"))
    plt.close()

    q1 = df_local[column].quantile(0.25)
    q3 = df_local[column].quantile(0.75)
    iqr = q3 - q1
    outliers = df_local[(df_local[column] < q1 - 1.5 * iqr) | (df_local[column] > q3 + 1.5 * iqr)]
    print(f"🔍 {column} - Outliers detected: {len(outliers)}")

def stationarity_tests(series, name="Close"):
    print(f"\n--- Stationarity Check: {name} ---")

    adf_stat, adf_p, _, _, adf_crit, _ = adfuller(series.dropna())
    print("ADF Test:")
    print(f"  Statistic: {adf_stat:.4f}, p-value: {adf_p:.4f}")
    print(f"  Critical Values: {adf_crit}")

    try:
        kpss_stat, kpss_p, _, kpss_crit = kpss(series.dropna(), regression='c', nlags="auto")
        print("KPSS Test:")
        print(f"  Statistic: {kpss_stat:.4f}, p-value: {kpss_p:.4f}")
        print(f"  Critical Values: {kpss_crit}")
    except Exception as e:
        print(f"⚠️ KPSS test failed: {e}")

def difference_until_stationary(df_local, col="Close"):
    series = df_local[col].dropna()
    d = 0
    while True:
        adf_p = adfuller(series)[1]
        kpss_p = kpss(series, regression='c', nlags="auto")[1]
        if adf_p < 0.05 and kpss_p > 0.05:
            print(f"✅ Stationarity achieved at d={d}")
            return series, d
        else:
            series = series.diff().dropna()
            d += 1
            if d > 5:
                print("❌ Stationarity not achieved within 5 differences.")
                break
    return series, d

if __name__ == "__main__":
    try:
        stock_df, root = load_and_prepare_data()

        detect_outliers(stock_df, "return", root)
        detect_outliers(stock_df, "Volume", root)

        stationarity_tests(stock_df["Close"], "Close")

        diff_series, d_order = difference_until_stationary(stock_df, "Close")
        print("\n✅ Final differencing order used:", d_order)

        # Save the cleaned and feature-engineered dataset
        processed_path = os.path.join(root, "data", "processed", "Tesla_Cleaned.csv")
        stock_df.to_csv(processed_path)
        print(f"✅ Cleaned dataset saved to: {processed_path}")

    except Exception as err:
        print(f"❌ Preprocessing pipeline failed: {err}")


