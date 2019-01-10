import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
warnings.filterwarnings('ignore') 
os.chdir('G:\\临时\\classdata')

# 查看数据
df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()

data = df[['event','name','height','arm','leg','gold','silver','bronze']]
data.dropna(inplace = True)

# 对数据进行整理
data['arm/h'] = data['arm'] / data['height']
data['leg/h'] = data['leg'] / data['height']
data = data[data['leg/h']<0.7]
data = data[data['arm/h']>0.7]

# 将各项指数标准化
data['leg_assess'] = data['leg/h']
data['arm_assess'] = np.abs(data['arm/h'] - 1)
data['leg_nor'] = (data['leg_assess'] - data['leg_assess'].min())/(data['leg_assess'].max()-data['leg_assess'].min())              
data['arm_nor'] = (data['arm_assess'].max() - data['arm_assess'])/(data['arm_assess'].max()-data['arm_assess'].min())
data['final'] = (data['leg_nor']+data['arm_nor'])/2
data['grade'] = data['gold']*3 + data['silver']*2 +data['bronze']

data_me = data[['event','name','final','grade']]
events = data['event'].value_counts().index.tolist()

# 将数据按照项目类型拆分
event_data = []
# for i in events:
#     data_i = data[data['event'] == i]  
#     event_data.append(data_i)
#     gi = sns.jointplot(x=data_i['arm/h'], y=data_i['leg/h'],data = data_i,
#                   kind="kde", color='k',   # 这里color = color中，第一个color为参数，第二个color为变量
#                   alpha = 0.6,shade_lowest=False)
#     gi.plot_joint(plt.scatter,c='w',s=15, linewidth=1, marker="+")
#     plt.title(i)

# 绘制二维散点图并导出图表
sns.set_style("darkgrid")
g = sns.jointplot(x=data['arm/h'], y=data['leg/h'],data = data,
                  kind="kde", color='k',   # 这里color = color中，第一个color为参数，第二个color为变量
                  alpha = 0.6,shade_lowest=False)
g.plot_joint(plt.scatter,c='w',s=15, linewidth=1, marker="+")
plt.savefig('pic3.png',dpi=400)

# 折线图————讨论手长脚长是否会影响运动员的成绩
# g = plt.scatter(x = data['grade'],y = data['final'],
#                 marker = 'o',c = 'g',alpha = '0.6')
# plt.xlabel('grade')
# plt.ylabel('leg/arm')
# plt.show()
# plt.savefig('q3-3.png',dpi=400)
color = ['g','y']
plt.figure(figsize = (12,5))
g = plt.scatter(data['grade'],data['final'],
                s = 40,marker = 'o',c = color, alpha = '0.6')
plt.grid(True)
plt.xlabel('grade')
plt.ylabel('leg/arm')
plt.title("Score--Stature?")
plt.show()
plt.savefig('q3-32.png',dpi=400)

# sns.set_style("darkgrid")
# g = sns.jointplot(x=data['grade'], y=data['final'],data = data,
#                   kind="kde", color='k',   # 这里color = color中，第一个color为参数，第二个color为变量
#                   alpha = 0.6,shade_lowest=False)
# g.plot_joint(plt.scatter,c='k',s=15, linewidth=1, marker="o")
# plt.title("Score--Stature?")
# plt.show()
# plt.savefig('q3-31.png',dpi=400)
