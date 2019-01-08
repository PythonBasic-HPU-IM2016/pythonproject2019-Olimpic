import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') 


import os
os.chdir('G:\\临时\\classdata')
# 创建工作路径

df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()
# 查看数据

data = df[['event','name','height','weight']]
# 筛选数据，按照目标字段筛选

event_count = data['event'].value_counts() 
event_drop = event_count[event_count<15]
data2 = data[data['event'] != 'swim']
data2.dropna(inplace = True)
# 数据清洗

data2['BMI'] = data2['weight']/(data2['height']/100)**2
data2['BMI_range'] = pd.cut(data2['BMI'],
                            [0,18.5,24,28,50], 
                            labels=["Thin", "Normal", "Strong",'ExtremelyStrong']) 
# 计算运动员BMI指数，并整理出BMI区间值

sns.set_style("ticks")
plt.figure(figsize = (8,4))  
sns.violinplot(x="event", y="BMI", data=data2,
               scale = 'count',      
               palette = "hls",     
               inner = "quartile")   
# 绘制小提琴图

sns.swarmplot(x="event", y="BMI", data=data2, color="w", alpha=.8,s=2)
# 绘制内部散点图

plt.grid(linestyle = '--')
plt.title("Athlete's BMI")
plt.show()
plt.savefig('pic2.png',dpi=400)