import numpy as np

arr = np.array([11,22,33,0.,44,55])
print(arr)
print(arr.sum())
print(arr.std())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.size)

print("..............................")

print(arr.nonzero())

print(arr.dtype)

print(np.all([1,2,3,4]))
print(np.all([1,2,0,3,4]))


print(np.any([1,2,3,4]))
print(np.any([1,2,0,3,4]))
print(np.any([0,0,0,0.,0]))
print(np.any([0,0,0,0.,0,1]))



n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print("\n\n")

print(n1)
print(n2)

print(n1+n2)
print(n2-n1)

n3 = np.array([4,5,6,7])

#print(n1+n3)   ValueError: operands could not be broadcast together with shapes (3,) (4,)



