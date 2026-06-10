from pathlib import Path
import pandas as pd

def summarize_table(path: str, max_rows: int = 5) -> str:
    file_path = Path(path).expanduser()
    if not file_path.exists():
        return f"File not found: {file_path}"

    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    lines = [
        f"File: {file_path.name}",
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        "Column names: " + ", ".join(map(str, df.columns)),
        "",
        "Preview:",
        df.head(max_rows).to_string(index=False),
    ]

    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        lines.extend(["", "Numeric summary:", numeric.describe().to_string()])

    return "\n".join(lines)
