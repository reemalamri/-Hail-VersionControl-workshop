import pandas as pd 
import sqlite3

data = pd.read_csv("iris.csv")
sum_data = data["PetalWidthCm"].sum() 
mean_data = data["PetalWidthCm"].mean() 
median_data = data["PetalWidthCm"].median() 
max_data = data["PetalWidthCm"].max()  
min_data = data["PetalWidthCm"].min()
midrange= (max_data + min_data)/ 2
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data, "\nmidrange:",midrange) 