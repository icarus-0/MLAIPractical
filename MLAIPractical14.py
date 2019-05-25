import numpy as np

a = np.array([1,2,3,4])
print()
print(a+1)
print()
print(a**2)

print()

a = np.array([1,2,3,4])
b = np.ones(4)+1

print(a)
print()
print(b)
print(a-b)
print(a*b)

print()

j = np.arange(5)

print(2**(j+1)-j)


a =np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = (a==b)
print(c)
print()
print(a==b)
print(a>b)



a =np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))


a = np.array([1,1,0,0],dtype=bool)
b = np.array([1,0,1,0],dtype=bool)
print(a)
print()
print(b)
print()
print(np.logical_or(a,b))
print(np.logical_and(a,b))



print(np.pi)

print()

print(np.linspace(-10,10,120))
print()

print(np.linspace(-np.pi,np.pi,256))
print()
print(np.linspace(0,1,20))
print()

a = np.arange(1,6)
print(np.sin(a))
print()

print(np.cos(a))
print()

print(np.log(a))
print()

print(np.exp(a))

print()

x = np.array([1,2,3,4])

print(np.sum(x))
print()
print(x.sum())

print("--------Sum by rows and the columns:---------")

x = np.array([[1,2],[3,4]])
print(x.sum(axis=0))
print()
print(x[:,0].sum(),x[:,1].sum())
print()
print(x.sum(axis=1))

print("----------extrema-------------")

x = np.array([1,3,2])
print(x.min())
print(x.max())


a  = np.zeros((10,10))

print(np.any(a!=0))
print(np.all(a==0))


a = np.array([1,2,3,2])
b = np.array([2,2,3,2])
print()

c = np.array([6,4,4,5])

print(((a<=b)&(b<=c)).all())



print()

print("--------statistics----------")
x = np.array([1,2,3,1,1])

print()

print(x.mean())
print(np.median(x))
print(x.std())