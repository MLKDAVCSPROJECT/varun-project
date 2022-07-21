import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv(r'C:\Users\admin\Desktop\ananya\IP project survey.csv', sep=',', header=0, names=['Name','Age(yrs)', 'Gender', 'Question 1', 'Question 2','InAge'])
df=pd.DataFrame(data,columns=['Name','Age(yrs)', 'Gender', 'Question 1', 'Question 2','InAge'])


x=int(input("Enter 1 for bar graph for Gender Analysis or 2 for line plot for Age Group Analysis or 3 for histogram for Overall Age Distribution Analysis: "))
if x==1:
   import matplotlib.pyplot as plt
   c=['total','increased','decreased','constant']
   a=[19,8,1,10]
   b=[11,4,0,7]
   plt.barh(c,a,color='aqua', label='Females')
   plt.barh(c,b,color='deeppink',  label='Males')
   plt.xticks(np.arange(1,25,1))
   plt.title('Gender Analysis') 
   plt.ylabel('Status')
   plt.xlabel('Number of Females/Males')
   plt.legend()
   plt.show()
   
elif x==2:
   y=str(input('Enter \'a\' for Age Group 15-18, \'b\' for Age Group 19-30 or \'c\' for Age Group 31-45: '))
   if y=='a':
      x=[1,9]
      y=[8,2]
      z=['Yes','No']
      plt.plot(z,x,color='teal',linewidth=5,label='Before Pandemic')
      plt.plot(z,y, color='darkviolet',linewidth=5,label='After Pandemic\'s Start')
      plt.grid(True)
      plt.ylabel('Frequency')
      plt.xlabel('Yes/No Anwer')
      plt.title('Age Group Analysis (15-18)')
      plt.legend()
      plt.show()
   elif y=='b':
      x=[4,6]
      y=[5,5]
      z=['Yes','No']
      plt.plot(z,x,color='gold',linewidth=5,label='Before Pandemic')
      plt.plot(z,y,color='darkred',linewidth=5,label='After Pandemic\'s Start')
      plt.title('Age Group Analysis (19-30)')
      plt.grid(True)
      plt.ylabel('Frequency')
      plt.xlabel('Yes/No Anwer')
      plt.legend()
      plt.show()
   elif y=='c':
      x=[0,10]
      y=[4,6]
      z=['Yes','No']
      plt.plot(z,x,linewidth=5,color='mediumvioletred',label='Before Pandemic')
      plt.plot(z,y,linewidth=5,color='darkgreen',label='After Pandemic\'s Start')
      plt.grid(True)
      plt.ylabel('Frequency')
      plt.xlabel('Yes/No Anwer')
      plt.title('Age Group Analysis (31-45)')
      plt.legend()
      plt.show()
   else:
      print('Kindly enter a valid option.')

elif x==3:
   x=[14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46] 
   z=[16,31,28,34,29,34,17,15,18,20,33,16,18,17,42,26,28,36,38,22,20,21,25,23,40,39,31,22,43,45]
   plt.hist(z,bins=x,edgecolor='k',color='lightblue',linewidth=3,hatch='..')
   plt.xticks(x)
   plt.yticks([0,1,2,3])
   plt.title('Age Distribution Analysis')
   plt.grid(False)
   plt.xlabel('Age (in Years)')
   plt.ylabel('Frequency')
   plt.show()
 
else:
   print('Kindly enter a valid number.')
   
z=str(input('Enter \'mean\' for Mean of Age (in Years),   \'median\' for Median of Age (in Years) or    \'mode\' for Mode  : '))
if z=='mean':
   print(df.mean(numeric_only=True))

elif z=='median':
   print(df.median(numeric_only=True))

elif z=='mode':
   a=int(input('Enter 1 for Mode of Age (in Years) Distribution, 2 for Mode of Age Group (in Years),  3 for Mode of Gender, 4 for Mode of Answers of Stress Pre- Pandemic or 5 for Mode of Answers of Stress Post-Pandemic: '))
   if a==1:
      print(df['InAge'].mode())
   elif a==2:
      print(df['Age(yrs)'].mode())
   elif a==3:
      print(df['Gender'].mode())
   elif a==4:
      print(df['Question 1'].mode())
   elif a==5:
      print(df['Question 2'].mode())
   else:
      print('Kindly enter a valid option.')

else:
   print('Kindly enter a valid option.')
