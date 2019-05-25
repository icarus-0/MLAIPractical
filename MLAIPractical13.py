import numpy as np

n = np.array([10,-1,0,90,300,3,-6,2])

print(n)
n.sort()  # In-place sorting

print("after sort")
print(n)

n = np.array([10,-1,0,90,300,3,-6,2])
#print(n)
n1 = n.argsort()
#print(n1)
#print(n.argsort())
#print(n)

for i in n1:
    print(n[i],end=" ")

print("\n")

print(n[n1])


na = np.array([[1,2,3],
              [4,5,6]])

print(na.transpose())

#print(np.eye(6))
a = np.ones(3)
a=a*3

i = np.eye(3)
b = np.dot(a,i)

print(b)
print("\n\n")


na = np.array([[1,2],
               [5,6]])
naa = np.dot(na,na)
print(na)
print("\n")

print(naa)