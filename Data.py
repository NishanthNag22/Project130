import csv
import pandas as pd

df=pd.read_csv('finalData.csv')
print(df.shape)
print(list(df))

del df["Unnamed: 0"]
del df["Unnamed: 5"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]

print(df.shape)
print(list(df))

df.to_csv("CleanedData.csv")