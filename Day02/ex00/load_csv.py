import pandas as pd


def load(path: str):
    #read the csv file using pandas get dimensions and rows of the dataset
    df = pd.read_csv(path)
    #separate the features and target variable
    #get the dimensions of the dataset
    print(f"Dataset dimensions: {df.shape}")
    print(f"First 5 rows:\n{df.head()}")
    return df
