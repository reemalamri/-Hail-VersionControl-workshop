import pandas as pd
import sqlite3
connection = sqlite3.connect('iris.db')
sql = 'SELECT SepalLengthCm, SepalWidthCm , Species FROM iris WHERE Species=?'
Species = ['Iris-setosa']
df = pd.read_sql_query(sql,connection,params=Species)
print('numper of row', len(df))
print(df.head(12))