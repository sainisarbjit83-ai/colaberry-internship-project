import pandas as pd

df = pd.read_csv("data/sample_data.csv")


print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

filtered_df = df[df['age'] > 27]
print(filtered_df)