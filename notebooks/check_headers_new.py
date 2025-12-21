import pandas as pd
from pathlib import Path

path = Path('../data/raw/creditcard.csv')
if path.exists():
    df = pd.read_csv(path, nrows=1)
    print(f"Columns: {df.columns.tolist()}")
else:
    print(f"File not found at {path.resolve()}")
