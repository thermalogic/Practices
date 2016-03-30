# coding=gbk
import xlrd
'''
Created on 2016年3月8日

@author: 1
'''
def mean(sample_list):#计算均值
    sum=0
    for i in sample_list:
        sum+=i
    mean_value=float(sum)/len(sample_list)
    return mean_value

def s_deviation(sample_list):#计算方差
    mean_value=mean(sample_list)
    s_deviation_value=0
    for i in range(len(sample_list)):
        sum1=((sample_list[i]-mean_value)**2)
        s_deviation_value+=sum1
    s_deviation_value=float(s_deviation_value)/len(sample_list)
    return s_deviation_value 
    
def linear_b(list_x,list_y):#计算相关系数b
    x_mean=mean(list_x)
    y_mean=mean(list_y)
    if len(list_x)!=len(list_y):
        print ("error")
    total=0
    total_=0
    for i in range(len(list_x)):
        sum1=list_x[i]*list_y[i]
        total+=sum1
        sum2=list_x[i]**2
        total_+=sum2
    s_xy=(float(total)/len(list_x))-(x_mean*y_mean)
    s_xx=(float(total_)/len(list_x))-x_mean
    return s_xy/s_xx

def linear_a(b,x_mean,y_mean):#计算相关系数a
    a=y_mean-b*x_mean     
    return a

data = xlrd.open_workbook('demo.xlsx')
table = data.sheets()[0]
ncols = table.ncols
a=table.col_values(0)
b=table.col_values(1)
c=table.col_values(2)
d=table.col_values(3)
print('第一列的均值' , mean(a))
print('第二列的均值' , mean(b))
print('第三列的均值' , mean(c))
print('第四列的均值' , mean(d))
print('第一列的方差' , s_deviation(a))
print('第二列的方差' , s_deviation(b))
print('第三列的方差' , s_deviation(c))
print('第四列的方差' , s_deviation(d))
b1=linear_b(a, b)
a1=linear_a(b1, mean(a), mean(b))
print('第一二列线性回归结果',a1,b1)
b2=linear_b(a,c)
a2=linear_a(b2,mean(a),mean(c))
print('第一三列线性回归结果',a2,b2)
b3=linear_b(a,d)
a3=linear_a(b3,mean(a),mean(d))
print('第一四列线性回归结果',a3,b3)
import numpy as np
import pylab as pl
x1=[0,-a1/b1]
y1=[a1,0]
pl.plot(x1,y1,'r')
pl.plot(a, b,'go')
pl.title('FIGURE1')
pl.show()
import pylab as pl_
x2=[0,-a2/b2]
y2=[a2,0]
pl_.plot(x2,y2,'r')
pl_.plot(a, c,'go')
pl_.title('FIGURE2')
pl_.show()
import pylab as pl__
x3=[0,-a3/b3]
y3=[a3,0]
pl__.plot(x3,y3,'r')
pl__.plot(a, d,'go')
pl__.title('FIGURE3')
pl__.show()