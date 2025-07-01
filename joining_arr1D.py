import numpy as np

n1 = np.array([1,2,3,4,5])
n2 = np.array([6,7,8,9,10])

for a in n1:
    print(a)
for a in n2:
    print(a)    

join = np.concatenate((n1, n2))
print("After join:\n", join)