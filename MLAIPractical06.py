
import pandas as pd
import urllib.request
hnames = ['sepal-length','sepal-width','petal-length','petal-width','class']

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
df = pd.read_csv(web_path,names=hnames)
print(df.shape)
print(df)

print(df.columns)