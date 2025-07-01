import numpy as np

n1 = np.array([5,10,15,20])
n2 = np.array([5,10,30,25])

print("Intersection of n1:")
for a in n1:
    print(a)

print("Intersection of n2:")    
for a in n2:
    print(a)
 
resarr = np.intersect1d(n1, n2)    
print("Intersection of n1 and n2:\n", resarr)
