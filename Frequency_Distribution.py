import pandas as pd 
import sqlite3
data = pd.read_csv("iris.csv")
value_co_data=data['Species'].value_counts()
print(value_co_data)
species_frequency3 = data.groupby(['Species']).size()
print("3", species_frequency3)
