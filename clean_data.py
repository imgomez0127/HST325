import pandas as pd 

df = pd.read_csv("Unemployment_Data.csv")
print(len(df))
df2 = df.drop(df[df["State/Area"] == "Los Angeles County"].index)
print(len(df2))