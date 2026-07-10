import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "data.csv")

print("--- Reading data with Pandas (.py script) ---")
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    print(df)
else:
    print(f"File not found at: {data_path}")
