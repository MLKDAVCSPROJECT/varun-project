import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varpro.csv')
import matplotlib.pyplot as plt
df.plot(kind='line', color=['red','green'],marker="X", markersize=10,linestyle="--",linewidth=3)
plt.title('Population vs Density(2001)')
plt.xlabel('States')
plt.ylabel('Population(in lakhs) and Density(per sq. km)')
ticks=df.index.tolist()
plt.xticks(ticks,df.States)
plt.grid(True)
plt.show()
