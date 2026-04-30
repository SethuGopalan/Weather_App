from pyspark.sql import  SparkSession


weather_data_procession=SparkSession.builder.appName("WeatherApp").getOrCreate()
print("Spark started")

df= weather_data_procession.read.csv("data/weather.csv",header=True,inferSchema=True)

df.show(5)
print("Columns:",df.columns)
print()
print("data types:", df.dtypes)
print()
print("row count :",df.count())
print()
print("Column count:",len(df.columns))
print()
df.printSchema()