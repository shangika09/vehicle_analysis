import pandas as pd

# show basic stats
def basic_stats(df):
    return df.describe()

# show ev sales by year
def ev_sales_by_year(df):
    return df.groupby("year")["ev_sales"].sum()

# show petrol sales by year
def petrol_sales_by_year(df):
    return df.groupby("year")["petrol_car_sales"].sum()

# show top 5 countries
def top_countries(df):
    return df.groupby("country")["ev_sales"].sum().sort_values(ascending=False).head(5)