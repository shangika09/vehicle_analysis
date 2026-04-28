import pandas as pd
def load_data():
    df = pd.read_csv("ev_vs_petrol_dataset_v3.csv")
    return df
