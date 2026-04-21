import pandas as pd 
def read_data():
    Wr_data=pd.read_csv("data/weather.csv")
    print(Wr_data.head(5))
    print(Wr_data.columns)
read_data()