import pandas as pd
def load_data():
    df = pd.read_csv("ev_vs_petrol_dataset_v3.csv")
    return df
def clean_data(df):
    df = df.dropna()
    return df
