#HOW TO LOAD MAACHINE LEARNING DATA

#1>LOAD CSV ILES WITH THE PYTHON STANDARD LIBRAARY
#2>LOAD CSV FILES WITH NUMPY
#3>LOAD THE CSV FILES WITH PANDAS

import csv
filename = open('indian-diabetes.data.csv','r')   #by te use of default reader function to open a csv file on python code
reader = csv.reader(filename,delimiter=',')   #reader will read the file lie by line
lines = list(reader)
print("\n\nNo of row:",len(lines),"\n\n")
print(lines)

for l in lines:
    print(l)