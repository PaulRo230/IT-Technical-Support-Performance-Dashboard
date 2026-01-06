import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "Bogdan.xlsx"

def load_data():
    df = pd.read_excel(DATA_PATH)

    df.columns = [c.strip() for c in df.columns]

    df["Month"] = df["Month"].replace("Feb-29", "Feb")

    month_order = ["Jan", "Feb", "Mar", "Apr"]
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

    return df