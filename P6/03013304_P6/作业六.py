# -*- coding: utf-8 -*- 
import xlrd    #打开EXCEL文件  
def average(excel_list):  #用以计算数据的平均值
    sum=0
    j=0                    #定义j以计算一共有多少组数据
    for i in excel_list:
        sum+=i
        j+=1
    return (float(sum)/j)
   
def variance(excel_list):
    mean=average(excel_list)
    tot=0
    k=0                    #定义k以计算一共有多少组数据
    for i in excel_list:
        tot+=(i-mean)**2
        k+=1
    return (float(tot)/k)**0.5

def r(x,y):        #用以计算皮尔逊相关系数r
    if len(x)!=len(y):
        print ('无法计算')
    tot1=0
    tot2=0
    tot3=0   
    for i in range(len(x)):
        sum1=x[i]-average(x)
        sum2=y[i]-average(y)
        tot1+=(sum1*sum2)
        sum3=(x[i]-average(x))**2
        sum4=(y[i]-average(y))**2
        tot2+=sum3
        tot3+=sum4
    return tot1/((tot2*tot3)**0.5)            
        
excel = xlrd.open_workbook('test.xlsx')  
sheet = excel.sheets()[0]     #获取第一个sheet    
ncols = sheet.ncols
l=[average(sheet.col_values(x)) for x in range(0,8)] #利用输出列表的方式获得表中各列的数据并将各列的均值输出
print ('第一到八列数据的平均值分别为：',l)
m=[variance(sheet.col_values(x)) for x in range(0,8)]
print ('第一到八列数据的方差分别为：',m) 
n=[r(sheet.col_values(2*x),sheet.col_values(2*x+1)) for x in range(0,4)]
print('相关系数：r1、r2、r3、r4分别为',n)

import matplotlib.pyplot as t1
import numpy as np
t1.figure(1) #创建图1
t1.title('figure')
ax1 = t1.subplot(221)
ax2 = t1.subplot(222)
ax3 = t1.subplot(223)
ax4 = t1.subplot(224)
t1.sca(ax1)
t1.xlabel('x')     #生成x轴
t1.ylabel('y')     #生成y轴
t1.plot(sheet.col_values(0), sheet.col_values(1),'bo')   #作散点图 1
x1 = np.array(sheet.col_values(0))          #pylab.array（）可以进行类型转换，将列表转换为数组类型
y1 = np.array(sheet.col_values(1))
m1,n1 = np.polyfit(x1, y1, 1)
predict_y1 = m1*np.array(x1) + n1
t1.plot(x1, predict_y1)                     #线性拟合直线

t1.sca(ax2)
t1.xlabel('x')     #生成x轴
t1.ylabel('y')     #生成y轴
t1.plot(sheet.col_values(2), sheet.col_values(3),'bo')   #作散点图 2
x2 = np.array(sheet.col_values(2))          #pylab.array（）可以进行类型转换，将列表转换为数组类型
y2 = np.array(sheet.col_values(3))
m2,n2 = np.polyfit(x2, y2, 1)
predict_y2 = m2*np.array(x2) + n2
t1.plot(x2, predict_y2)                     #线性拟合直线

t1.sca(ax3)
t1.xlabel('x')     #生成x轴
t1.ylabel('y')     #生成y轴
t1.plot(sheet.col_values(4), sheet.col_values(5),'bo')   #作散点图 3
x3 = np.array(sheet.col_values(4))          #pylab.array（）可以进行类型转换，将列表转换为数组类型
y3 = np.array(sheet.col_values(5))
m3,n3 = np.polyfit(x3, y3, 1)
predict_y3 = m3*np.array(x3) + n3
t1.plot(x3, predict_y3)                     #线性拟合直线

t1.sca(ax4)
t1.xlabel('x')     #生成x轴
t1.ylabel('y')     #生成y轴
t1.plot(sheet.col_values(6), sheet.col_values(7),'bo')   #作散点图 4
x4 = np.array(sheet.col_values(6))          #pylab.array（）可以进行类型转换，将列表转换为数组类型
y4 = np.array(sheet.col_values(7))
m4,n4 = np.polyfit(x4, y4, 1)
predict_y4 = m4*np.array(x4) + n4
t1.plot(x4, predict_y4)                     #线性拟合直线

t1.show()            #绘制图线