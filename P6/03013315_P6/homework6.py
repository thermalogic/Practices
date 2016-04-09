#-*- coding: utf8 -*-
import xlrd
import pylab
import numpy
import numpy as np
from scipy import stats

fname = "sheet.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print( "no sheet in %s named Sheet1" % fname)
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print( "nrows %d, ncols %d" % (nrows,ncols))


col_list=[]
#获取各行数据
for i in range(0,ncols):
    col_data = sh.col_values(i)
    col_list.append(col_data)

x1=col_list[0]
xp1=numpy.var(x1)
xf1=numpy.mean(x1)
print('表1中x平均值=',xp1)
print('表1中x方差=',xf1)
y1=col_list[1]
yp1=numpy.var(y1)
yf1=numpy.mean(y1)
print('表1中y平均值=',yp1)
print('表1中y方差=',yf1)
xy1=numpy.correlate(col_list[0],col_list[1])
print('表1中xy相关系数=',xy1[0])

x2=col_list[2]
xp2=numpy.var(x2)
xf2=numpy.mean(x2)
print('表2中x平均值=',xp2)
print('表2中x方差=',xf2)
y2=col_list[3]
yp2=numpy.var(y2)
yf2=numpy.mean(y2)
print('表2中y平均值=',yp1)
print('表2中y方差=',yf1)
xy2=numpy.correlate(col_list[2],col_list[3])
print('表2中xy相关系数=',xy2[0])

x3=col_list[4]
xp3=numpy.var(x3)
xf3=numpy.mean(x3)
print('表3中x平均值=',xp3)
print('表3中x方差=',xf3)
y3=col_list[5]
yp3=numpy.var(y3)
yf3=numpy.mean(y3)
print('表3中y平均值=',yp3)
print('表3中y方差=',yf3)
xy3=numpy.correlate(col_list[4],col_list[5])
print('表3中xy相关系数=',xy3[0])

x4=col_list[6]
xp4=numpy.var(x4)
xf4=numpy.mean(x4)
print('表4中x平均值=',xp4)
print('表4中x方差=',xf4)
y4=col_list[7]
yp4=numpy.var(y4)
yf4=numpy.mean(y4)
print('表4中y平均值=',yp4)
print('表4中y方差=',yf4)
xy4=numpy.correlate(col_list[6],col_list[7])
print('表4中xy相关系数=',xy4[0])

x1=np.array(col_list[0])
y1=np.array(col_list[1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x1, y1)

predict_y1 = intercept + slope * x1
pred_error = y1 - predict_y1
degrees_of_freedom = len(x1) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.figure(1)
pylab.plot(x1, y1, 'o')
pylab.plot(x1, predict_y1, 'k-')
pylab.show()

x2=np.array(col_list[2])
y2=np.array(col_list[3])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x2, y2)

predict_y2 = intercept + slope * x2
pred_error = y2 - predict_y2
degrees_of_freedom = len(x2) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.figure(2)
pylab.plot(x2, y2, 'o')
pylab.plot(x2, predict_y2, 'k-')
pylab.show()

x3=np.array(col_list[4])
y3=np.array(col_list[5])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x3, y3)

predict_y3 = intercept + slope * x3
pred_error = y3 - predict_y3
degrees_of_freedom = len(x3) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.figure(3)
pylab.plot(x3, y3, 'o')
pylab.plot(x3, predict_y3, 'k-')
pylab.show()

x4=np.array(col_list[6])
y4=np.array(col_list[7])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x4, y4)

predict_y4 = intercept + slope * x4
pred_error = y4 - predict_y4
degrees_of_freedom = len(x4) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.figure(4)
pylab.plot(x4, y4, 'o')
pylab.plot(x4, predict_y4, 'k-')
pylab.show()
