import numpy as np

n = np.array([1,2,3,4,5,6])

print("Iterating: ")
for a in n:
    print(a)

search = np.where(n == 3)
print("Search result for 3:", search)    