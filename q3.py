import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') 
# 不发出警告

import os
os.chdir('G:\\临时\\classdata')
# 创建工作路径

df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()
# 查看数据

data = df[['event','name','height','arm','leg']]
data.dropna(inplace = True)   # 去掉缺失值
# 筛选数据，按照目标字段筛选

data['arm/h'] = data['arm'] / data['height']
data['leg/h'] = data['leg'] / data['height']
data = data[data['leg/h']<0.7]
data = data[data['arm/h']>0.7]

events = data['event'].value_counts().index.tolist()
# 提取样本数据的所有项目

event_data = []
for i in eventlst:
    data_i = data[data['event'] == i]  
    event_data.append(data_i)
    gi = sns.jointplot(x=data_i['arm/h'], y=data_i['leg/h'],data = data_i,
                  kind="kde", color='k',   # 这里color = color中，第一个color为参数，第二个color为变量
                  alpha = 0.6,shade_lowest=False)
    gi.plot_joint(plt.scatter,c='w',s=15, linewidth=1, marker="+")
    plt.title(i)
# 将数据按照项目类型拆分

sns.set_style("darkgrid")

g = sns.jointplot(x=data['arm/h'], y=data['leg/h'],data = data,
                  kind="kde", color='k',   # 这里color = color中，第一个color为参数，第二个color为变量
                  alpha = 0.6,shade_lowest=False)
g.plot_joint(plt.scatter,c='w',s=15, linewidth=1, marker="+")
plt.savefig('pic3.png',dpi=400)
# 绘制二维散点图并导出图表
