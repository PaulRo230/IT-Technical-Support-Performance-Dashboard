import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "Bogdan.xlsx"

df = pd.read_excel(DATA_PATH)

new_rows = pd.DataFrame([
    [1990, "29-Apr", "Apr", "Olympia", "hardware", 59.9, 23.1],
    [1994, "29-Apr", "Apr", "Spokane", "hardware", 15.8, 64.1],
    [2000, "29-Apr", "Apr", "Bellingham", "hardware", 26.7, 53.4],
    [2005, "29-Apr", "Apr", "Bellingham", "internet", 41.4, 12.8],
    [2011, "30-Apr", "Apr", "Olympia", "hardware", 96.1, 14.6],
    [2012, "30-Apr", "Apr", "Spokane", "hardware", 125.6, 55.0],
    [2019, "30-Apr", "Apr", "Spokane", "email", 4.5, 45.9],
], columns=df.columns)

df = pd.concat([df, new_rows], ignore_index=True)
df.to_excel(DATA_PATH, index=False)