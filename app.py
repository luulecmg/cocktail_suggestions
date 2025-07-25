import pandas as pd

df = pd.read_csv("data/final_cocktails.csv", index_col=0)
print(df.head())
