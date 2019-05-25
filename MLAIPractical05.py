#importing csv file in our python code with the use of pandas



import pandas as pd

df = pd.read_csv('indian-diabetes.data.csv', header=0)
print(df)
#print(df.head())
print(df.describe())
