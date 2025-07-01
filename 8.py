import pandas as pd

data1 = [10, 20, 30, 40, 50]
data2 = [60, 70, 80, 90, 100]

series1 = pd.Series(data1)
series2 = pd.Series(data2)

print("Series 1:", series1)
print("Series 2:", series2)

def demo (x1, x2):
    if(x1 > x2):
        return x1
    else:
        return x2
    
res = series1.combine(series2, demo)

print(res)