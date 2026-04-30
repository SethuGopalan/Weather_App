from pyspark.sql import  SparkSession


weather_data_procession=SparkSession.builder.appName("WeatherApp").getOrCreate()
print("Spark started")

df= weather_data_procession.read.csv("data/weather.csv",header=True,inferSchema=True)

df.show(5)
df.printSchema()