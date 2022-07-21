import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varproject.csv')
import matplotlib.pyplot as plt
df.plot(kind='line', color=['red','green'],marker="X", markersize=10,linestyle="--",linewidth=3)
plt.title('Population vs Density(2011)')
plt.xlabel('States')
plt.ylabel('Population(in 1000) and Density(per sq. km)')
ticks=df.index.tolist()
plt.xticks(ticks,df.States)
plt.grid(True)
plt.show()
