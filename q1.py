import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os


os.chdir('G:\\classdata')
warnings.filterwarnings('ignore') 

# 查看数据
df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()

# 数据处理
data = df[['event','name','gender','height']]
data.dropna(inplace = True)  
data_male = data[data['gender'] == '男']
data_female = data[data['gender'] == '女']

hmean_male = data_male['height'].mean()
hmean_female = data_female['height'].mean()
femal_max=data_female['height'].max()
male_max = data_male['height'].max()

# 绘制折线图
sns.set_style("ticks")
plt.figure(figsize = (8,4))  
sns.distplot(data_male['height'],hist = False,kde = True,rug = True,
             rug_kws = {'color':'y','lw':2,'alpha':0.5,'height':0.1} ,   
             kde_kws={"color": "y", "lw": 1.5, 'linestyle':'--'},       
             label = 'male_height')
sns.distplot(data_female['height'],hist = False,kde = True,rug = True,
             rug_kws = {'color':'g','lw':2,'alpha':0.5} , 
             kde_kws={"color": "g", "lw": 1.5, 'linestyle':'--'},
             label = 'female_height')

# 绘制男运动员平均身高辅助线和男运动员最高身高备注
plt.axvline(hmean_male,color='y',linestyle=":",alpha=0.8) 
plt.text(hmean_male+2,0.003,'male_height_mean: %.1fcm' % (hmean_male), color = 'y')
plt.text(male_max +2,0.004,'male_height_max: %.1fcm' % (male_max), color = 'y')

# 绘制女运动员平均身高辅助线和女运动员最高身高备注
plt.axvline(hmean_female,color='g',linestyle=":",alpha=0.8)
plt.text(hmean_female+2,0.008,'female_height_mean: %.1fcm' % (hmean_female), color = 'g')
plt.text(femal_max+2,0.006,'female_height_max: %.1fcm' % (femal_max), color = 'g')

plt.ylim([0,0.03])
plt.grid(linestyle = '--')     
plt.title("Athlete's height")  

plt.savefig('q1.png',dpi=400)
