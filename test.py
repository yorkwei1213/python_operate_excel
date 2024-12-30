# coding: utf-8
import pandas as pd

df = pd.read_excel('tp.xlsx')  # 读取xlsx中第一个sheet
data1 = df.head(7)  # 读取前7行的所有数据，dataFrame结构
data2 = df.values  # list形式，读取表格所有数据

data3 = df.iloc[5:171].values

for i in data3:
    print("else if (vol >= %s){return %s;}" % (i[5], i[0][:-2]))