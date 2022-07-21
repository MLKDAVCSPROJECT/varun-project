import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varpro.csv')
import matplotlib.pyplot as plt
df.plot(kind='bar', x='States', title='Popuation vs Density(2001)', color=['blue', 'magenta'], edgecolor='Black', linewidth=1)
plt.ylabel('Population(in lakhs) and Density(per sq. km)')
plt.grid(True)
plt.show()
