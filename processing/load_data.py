import pandas as pd 
def read_data():
    Wr_data=pd.read_csv("data/weather.csv")
    print(Wr_data.head(5))
    print(Wr_data.columns)
    print(f" row count is : {len(Wr_data)}")
    print(f"Column count{len(Wr_data.columns)}")
    print(f"Null columns in the data: {Wr_data.columns.isnull().sum()}")
    print(f"shape of the data : {Wr_data.shape}")

read_data()