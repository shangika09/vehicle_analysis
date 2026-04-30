import sqlite3
import pandas as pd

# save data to database
def create_database(df):
    conn = sqlite3.connect("vehicle.db")
    df.to_sql("vehicles", conn, if_exists="replace", index=False)
    conn.close()

# get ev sales by year
def query_ev_sales():
    conn = sqlite3.connect("vehicle.db")
    result = pd.read_sql("SELECT year, SUM(ev_sales) FROM vehicles GROUP BY year", conn)
    conn.close()
    return result

# get top 5 countries
def query_top_countries():
    conn = sqlite3.connect("vehicle.db")
    result = pd.read_sql("SELECT country, SUM(ev_sales) FROM vehicles GROUP BY country ORDER BY SUM(ev_sales) DESC LIMIT 5", conn)
    conn.close()
    return result