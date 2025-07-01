import numpy as np

n1 = np.array([5,10,15,20,25,30,35,40,45,50])
n2 = np.array([1,2,3,4,5,6,7,8,9,10,45])

print("Difference of n1:")
for a in n1:
    print(a)

print("Difference of n2:")    
for a in n2:
    print(a)

ressr = np.setdiff1d(n1,n2) 
print("Difference of n1 and n2:\n", ressr)