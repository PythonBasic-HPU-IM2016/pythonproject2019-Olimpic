import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

os.chdir('G:\\临时\\classdata')
warnings.filterwarnings('ignore')

# 查看数据
df = pd.read_excel('奥运运动员数据.xlsx',sheetname=1,header=0)
df_length = len(df)
df_columns = df.columns.tolist()


data = df[['event','name','birthday']]
data.dropna(inplace = True)

data.index = pd.to_datetime(data['birthday'])   # 将出生年月改为时间序列
data['birthyear'] = data.index.year
data['age'] = 2016 - data['birthyear']
data['age_range'] = pd.cut(data['age'],
                          [0,26,60],
                          labels=["90s", "not 90s"])

sns.set_style("ticks")

# g = sns.FacetGrid(data, col="event", hue = 'age_range',palette="Set2_r",
#                   size=2.5,
#                   aspect=1.2,
#                  col_wrap=3,sharex=False,
#                 xlim=[15,40], ylim=[0,14])

# g.map(sns.stripplot,"age",jitter=True,
#      size = 10, edgecolor = 'w',linewidth=1,marker = 'o')
# g.add_legend()
# plt.savefig('pic5.png',dpi=400)

# 散点图在最后答辩的时候可以用来引出折线图，能大概的说明一个趋势
# 用散点图不能很好的反映数据，反映问题，经过多次的调试，最终又改为折线图。
data['age_range'] = pd.cut(data['age'],
                          [0,26,36,46],
                          labels=[1,2,3])
data2 = data.groupby(['event','age_range']).count()
data2.reset_index(inplace=True)
data2.fillna(0,inplace = True)
data2['count'] = data2['name']

g = sns.FacetGrid(data2, col="event", col_wrap=3,
                  size=2.5,
                  aspect=1.2,sharex=False,)
g.map(plt.plot, "age_range", "count",
      marker="o",color = 'gray',linewidth = 2)

g.set(xlim = (0,4),
      ylim = (-10,40),
      xticks = [0,1,2,3,4],
      xticklabels = ['',"90s", "80s","70s",''],
      yticks = [0,10,20,30,40])

g.add_legend()
plt.show()
plt.savefig('q4.png',dpi=400)

# 经过计算一些数值更直观的得到结论
ct90 = 0
ct80 = 0
ct70 = 0
data90 = data2[data2['age_range'] == 1]
data80 = data2[data2['age_range'] == 2]
data70 = data2[data2['age_range'] == 3]
for i in data90['count']:
    ct90 += i
for i in data80['count']:
    ct80 += i
for i in data70['count']:
    ct70 += i
print("90后运动员所占比例为:{:.4f},80后运动员所占比例为:{:.4f},70后运动员所占比例为:{:.4f}".format(ct90/df_length,ct80/df_length,ct70/df_length))
# 90后：44.78%，80后：51.30%，70后：3.48%
