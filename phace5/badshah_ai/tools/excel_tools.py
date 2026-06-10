from pathlib import Path
import pandas as pd

def summarize_table(path):
    p = Path(path).expanduser()
    if not p.exists():
        return "File not found"
    df = pd.read_csv(p) if p.suffix.lower()==".csv" else pd.read_excel(p)
    return f"Rows: {len(df)}\nColumns: {len(df.columns)}\n{df.head().to_string(index=False)}"
