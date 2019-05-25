import pandas as pd

filename = "indian-diabetes.data.csv"

hname = ['preg','plas','pres','skin','test','mass','pedi','age','class']

df = pd.read_csv(filename,names=hname)

print(df.head(20))

print("---*---"*10)


print("dataframe.shape:",df.shape)
print("---*---"*10)



print(df.dtypes)
print("---*---"*10)

pd.set_option('precision',2)

print("description=\n",df.describe())
print("---*---"*20)

print()

class_counts = df.groupby('class').size()
print(class_counts)
print("---*---"*20)


correlations = df.corr(method='pearson')
print(correlations)