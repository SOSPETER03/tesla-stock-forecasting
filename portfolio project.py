# scripts/data_cleaning.py

import matplotlib.pyplot as plt
import pandas as pd
import os

# Create results directory if it doesn't exist
results_dir = r"C:\Users\sospeter\PycharmProjects\pythonProject\tesla-stock-forecasting\results"
os.makedirs(results_dir, exist_ok=True)

# Load dataset
file_path = r"C:\Users\sospeter\PycharmProjects\pythonProject\tesla-stock-forecasting\Tasla_Stock_Updated_V2.csv"
df = pd.read_csv(file_path)

# Preview the data
print("🔍 First 5 rows:")
print(df.head())

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Sort by date just in case
df.sort_index(inplace=True)

# Check for missing values
print("\n🧼 Missing values:")
print(df.isnull().sum())

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\n📛 Number of duplicate rows: {duplicates}")

# Data types
print("\n📊 Data types:")
print(df.dtypes)

# Plot closing price for sanity check
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='Tesla Closing Price', color='purple')
plt.title('Tesla Closing Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig(os.path.join(results_dir, "tesla_stock_price.png"),
            dpi=300,
            bbox_inches='tight')

# Close the figure to free memory
plt.close()

# Show a message to confirm the save
print("\n✅ Figure saved successfully!")