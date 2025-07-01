import pandas as pd
import matplotlib.pyplot as plt
data ={
    "Player": ["maccullum", "stokes", "root", "buttler", "wood"],
    "Runs": [100, 200, 150, 180, 120],
    "Rank": [1, 2, 3, 4, 5],
    "Country": ["NZ", "ENG", "ENG", "ENG", "ENG"],
    "Age": [40, 30, 32, 35, 28]
}
 
df = pd.DataFrame(data,index = ["Player1", "Player2", "Player3", "Player4", "Player5"])

df.plot.pie(y="Runs")
plt.show()