import pandas as pd


def load(path: str):
    #read the csv file using pandas get dimensions and rows of the dataset
    df = pd.read_csv(path)
    return df
