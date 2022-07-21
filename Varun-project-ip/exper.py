import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varproject.csv')
import matplotlib.pyplot as plt
df.plot(kind='bar', x='States', title='Popuation vs Density(2011)', color=['blue', 'magenta'], edgecolor='Black', linewidth=1)
plt.ylabel('Population(in 1000) and Density(per sq. km)')
plt.grid(True)
plt.show()
