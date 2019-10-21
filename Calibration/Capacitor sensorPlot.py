import pandas as pd
import matplotlib.pyplot as plt
File1='FetBind.csv'
File2='FetNonBind.csv'
WorkingPath='C:\\Users\\Kotsos\\Desktop\\'
df=pd.read_csv(WorkingPath+File1,header=None)
df[0]=df[0].div(310) #Convert to volt
df.reset_index(inplace=True) 
df['index']=df['index']*2 #Convert to second
df.set_index('index',inplace=True)
df.plot(linewidth=1.5)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend().remove()
df=pd.read_csv(WorkingPath+File2,header=None)
df[0]=df[0].div(310)
df.reset_index(inplace=True)
df['index']=df['index']*2
df.set_index('index',inplace=True)
df.plot(linewidth=1.5)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend().remove()
plt.show()
