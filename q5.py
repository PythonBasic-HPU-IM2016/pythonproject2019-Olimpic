
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings('ignore') 


import os
os.chdir('C:\\Users\\Hjx\\Desktop\\')


df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()


#分析运动员全样本数据的身材分布情况


data = df[['event','name','birthday','height','arm','leg','weight','age']]
data.dropna(inplace = True)   # 去掉缺失值


data['BMI'] = data['weight']/(data['height']/100)**2   
# 求BMI

data['arm/h'] = data['arm'] / data['height']
data['leg/h'] = data['leg'] / data['height']
data = data[data['leg/h']<0.7]
data = data[data['arm/h']>0.7]
# 分别计算“臂展/身高”、“腿长/身高”，并删除异常数据

data_re = data[['event','name','arm/h','leg/h','BMI','age']]
# 重新新建结果数据data_re

data_re['BMI_assess'] = np.abs(data['BMI'] - 22)   
data_re['leg_assess'] = data['leg/h']             
data_re['arm_assess'] = np.abs(data['arm/h'] - 1) 
data_re['age_assess'] = data['age']            

data_re['BMI_nor'] = (data_re['BMI_assess'].max() - data_re['BMI_assess'])/(data_re['BMI_assess'].max()-data_re['BMI_assess'].min())
data_re['leg_nor'] = (data_re['leg_assess'] - data_re['leg_assess'].min())/(data_re['leg_assess'].max()-data_re['leg_assess'].min())              
data_re['arm_nor'] = (data_re['arm_assess'].max() - data_re['arm_assess'])/(data_re['arm_assess'].max()-data_re['arm_assess'].min()) 
data_re['age_nor'] = (data_re['age_assess'].max() - data_re['age_assess'])/(data_re['age_assess'].max()-data_re['age_assess'].min())
# 标准化

data_re['final'] = (data_re['BMI_nor']+data_re['leg_nor']+data_re['arm_nor']+data_re['age_nor'])/4
# 计算总体评价结果

plt.figure(figsize = (10,6))
data_re.sort_values(by = 'final',inplace = True,ascending=False)
data_re.reset_index(inplace=True)·# 重新设定index

data_re[['age_nor','BMI_nor','leg_nor','arm_nor']].plot.area(colormap = 'PuRd',alpha = 0.5,figsize = (10,6))
plt.ylim([0,4])
plt.grid(linestyle = '--')
plt.savefig('pic7.png',dpi=400)#导出图片


#top8具体


datatop8 = data_re[:8]


fig = plt.figure(figsize=(15,6))
plt.subplots_adjust(wspace=0.35,hspace=0.5)

#for循环绘制8位运动员身材指数的极轴图
n = 0
for i in datatop8['name'].tolist():
    n += 1
    c = plt.cm.BuPu_r(np.linspace(0, 0.7,10))[n-1]
    axi = plt.subplot(2,4,n, projection = 'polar')
    datai = datatop8[['BMI_nor','leg_nor','arm_nor','age_nor']][datatop8['name']==i].T
    scorei = datatop8['final'][datatop8['name']==i]
    angles = np.linspace(0, 2*np.pi, 4, endpoint=False)
    #axi.plot(angles,datai,linestyle = '-',lw=1,color = c)
    plt.polar(angles, datai, 'o-', linewidth=1,color = c)
    axi.fill(angles,datai,alpha=0.5,color=c)
    axi.set_thetagrids(np.arange(0.0, 360.0, 90),['BMI','腿长/身高','臂长/身高','年龄'])
    axi.set_rgrids(np.arange(0.2,1.5,0.2),'--')
    plt.title('Top%i %s: %.3f\n' %(n,i,scorei))


plt.savefig('pic8.png',dpi=400)



#不同项目的运动员身材情况

#绘制箱型图+散点图
plt.figure(figsize = (12,6))  
sns.boxplot(x="event", y="final",data = data_re,
            linewidth = 1,  
            width = 0.6,   
            fliersize = 2,
            palette = 'YlGnBu',
            whis = 1.5,      
            #order = ['Thur','Fri','Sat','Sun'],  
           )
sns.swarmplot(x="event", y="final",data = data_re,color ='k',size = 3,alpha = 0.8)
plt.grid(linestyle = '--')
plt.ylabel('Final score')
plt.savefig('pic9.png',dpi=400)# 图表导出
