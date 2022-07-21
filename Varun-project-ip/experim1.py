import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varpro.csv')
import matplotlib.pyplot as plt
df.plot(kind='hist', title='Population vs Density(2001)', color=['red','pink'], grid=(True), edgecolor='Black', linewidth=1)
plt.xlabel('Population(in lakhs)')
plt.ylabel('Density(per sq. km)')
plt.show()
