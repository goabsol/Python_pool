import pandas as pd


def load(path: str):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    except Exception as e:
        print(f"Error loading file: {e}")
        return
