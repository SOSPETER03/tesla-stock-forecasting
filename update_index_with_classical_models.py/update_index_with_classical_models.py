import os

# Absolute path to your index.md file
index_path = "C:/Users/sospeter/PycharmProjects/pythonProject/tesla-stock-forecasting/docs/index.md"

# Link to be added (adjust if you change the filename/location)
link_text = "\n- [Classical Time Series Modeling](../notebooks/classical_models.ipynb)"

try:
    if os.path.exists(index_path):
        with open(index_path, "a", encoding="utf-8") as f:
            f.write(link_text)
        print("✅ Successfully appended classical model link to index.md")
    else:
        print(f"❌ File not found at path: {index_path}")
except Exception as error:
    print(f"⚠️ Failed to update index.md: {error}")
