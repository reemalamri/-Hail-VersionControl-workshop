import pandas as pd 
import sqlite3

connection = sqlite3.connect('iris.db')
#load data to python
sql = """SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species FROM iris"""
df = pd.read_sql_query(sql,connection)

Species_group=df.groupby(['Species'])
iris_min=Species_group.min()
iris_max=Species_group.max()

print('iris minimums')
print(iris_min)
print()
print('iris maximums')
print(iris_max)
