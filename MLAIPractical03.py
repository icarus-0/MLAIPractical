#importing the data csv file in our python package by using Numpy package


import numpy as np
filename = 'indian-diabetes.data.csv'

raw_data = open(filename,'r')

data = np.loadtxt(raw_data,delimiter=",")

print("Numpy loadTXt:",data.shape)

raw_data.close()

print("\n\n\n")

for l in data:
    print(l)