import numpy as np

a = np.array([[1,2],[3,4,5]])

print(a.shape)
print(a.size)

print()

d1 = np.array([[1,2],
               [3,4],
              [5,6],
              [7,8],
              [9,10],
              [11,12],
              [13,14]])

print(d1)

print(d1.shape)
print(d1.size)

#print(d1[: :2,0])

zr = np.zeros([3,4])

#print(zr)

zr1 = np.ones([6,6])*6

#print(zr1)

#print(zr1.dtype)

ar = np.arange(1,6)

print(ar)