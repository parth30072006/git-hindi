import pandas as pd
import numpy as np

data = [10 , 20 , 30, 40, 50, np.nan]

s = pd.Series(data)
print(s)
print(s.hasnans)