import pandas as pd
df=pd.read_csv(r'C:\Users\VARUN\Desktop\varproject.csv')
import matplotlib.pyplot as plt
df.plot(kind='hist', title='Population vs Density(2011)', color=['red','pink'], grid=(True), edgecolor='Black', linewidth=1)
plt.xlabel('Population(in 1000)')
plt.ylabel('Density(per sq. km)')
plt.show()
