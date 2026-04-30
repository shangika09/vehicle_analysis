import matplotlib.pyplot as plt

# line chart
def line_chart(df):
    df.groupby("year")["ev_sales"].sum().plot()
    plt.title("EV Sales by Year")
    plt.show()

# bar chart
def bar_chart(df):
    df.groupby("year")["petrol_car_sales"].sum().plot(kind="bar")
    plt.title("Petrol Sales by Year")
    plt.show()

# pie chart
def pie_chart(df):
    df.groupby("country")["ev_sales"].sum().head(5).plot(kind="pie")
    plt.title("Top 5 Countries EV Sales")
    plt.show()