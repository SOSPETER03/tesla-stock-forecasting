import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL, seasonal_decompose

# --- Corrected root path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
csv_path = os.path.join(project_root, "data", "processed", "Tesla_Cleaned.csv")
figs_path = os.path.join(project_root, "results", "figures")
os.makedirs(figs_path, exist_ok=True)

# --- Load data
df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')
df = df.asfreq('D')
df['Close'] = df['Close'].interpolate(method='linear')


# --- Classical Decomposition
classical_decomp = seasonal_decompose(df['Close'], model='multiplicative', period=12)
plt.figure(figsize=(12, 8))
classical_decomp.plot()
plt.suptitle("Classical Decomposition of Tesla Stock (Multiplicative)", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(figs_path, "classical_decomposition.png"))
plt.close()

# --- STL Decomposition
stl = STL(df['Close'], period=12, robust=True)
res = stl.fit()
fig = res.plot()
fig.suptitle("STL Decomposition of Tesla Stock", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(figs_path, "stl_decomposition.png"))
plt.close()

print("✅ STL and Classical decomposition plots saved to results/figures/")
