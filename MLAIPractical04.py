#   importing online data in our python code

import numpy as np

import urllib.request


web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

dataset = np.genfromtxt(web_path,delimiter=",")   # genfromtxt = generate from text

for l in dataset:
    print(l)




print("shape of data frpm url : ",dataset.shape)