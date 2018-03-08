## Practice 4

**Data Analysis**(15)：Statistics, regression and visualization

* Deadline: 2018.05.29

## Problem

John V. Guttag. Introduction to Computation and Programming Using Python. Revised and expanded edition. MIT Press. 2013.08.  

**16.4 Statistical Measures Don't, Tell the Whole Story**（Page226-227） 
  * In 1973, the statistician F.J. Anscombe published a paper containing the table below. It contains the <x, y> coordinates of the points in each of four data sets.

|x0 |y0|x1|y2|x2|y2|x3|y3|
| ---- |:------:| :------:| :------:|  :------:| :------:| :------:|  ----:|
|10.0|	8.04 |	10.0|	9.14 |	10.0 	|7.46	|8.0    |6.58|
|8.0| 	6.95 |	8.0 |	8.14 |	8.0     |6.77	|8.0    |5.76|
|13.0| 	7.68 |	13.0|	8.74 |	13.0    |12.74	|8.0    |7.71|
|9.0|	8.81 |	9.0 |	8.77 |	9.0     |7.11	|8.0    |8.84|
|11.0| 	8.33 |	11.0|	9.26|	11.0    |7.81	|8.0    |8.47|
|14.0| 	9.96 |	14.0|	8.10 |	14.0    |8.84	|8.0    |7.04|
|6.0|	7.24 |	6.0 |	6.13 |	6.0     |6.08	|8.0 	|5.25|
|4.0| 	4.26 |	4.0 |	3.10| 	4.0     |5.39	|19.0 	|12.5|
|12.0|	10.84| 	12.0| 	9.13| 	12.0    |8.15	|8.0 	|5.56|
|7.0| 	4.82 | 	7.0 |	7.26| 	7.0     |6.42	|8.0 	|7.91|
|5.0| 	5.68 | 	5.0 | 	4.74| 	5.0     |5.73	|8.0 	|6.89|

## 要求(15分)：

  使用Python文件或Jupyter Notebook实现。

* 1 四组数据的数据文件(1分)：纯文本格式或MS Excel表格；

* 2 数据分析对象表达(4分)：从数据文件读取数据,形成数据分析对象

* 3 统计指标(2分)：从数据文件读取数据，计算均值、方差和相关系数等统计指标

* 4 回归分析(3分): 线性回归

* 5 结果输出(5分): 数据点图和回归曲线(3分)；统计和回归结果(2分)

## 提交：

* 1 电邮：cmh@seu.edu.cn 
  * 主题：学号-姓名-4
  * 附件：程序文件压缩包：**学号-姓名-4.zip**

* 2 截至时间： 2018.05.29
  *  截至时间后可补交，补交得分<=10.(2018.06.15)

* 3  改进更新：提交作业后可改进，改进截至时间：2018.06.15

## 提示：

* 参考第11、15章

  * http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/11_PLOTTING_AND_MORE_ABOUT_CLASSES.ipynb
  * http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/15_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb

* 统计指标计算、回归分析: 可使用Python统计库、Numpy和Scipy

* 绘制数据点图: 使用Matplotlib

```python
    import numpy as np
    import matplotlib.pyplot as plt
    from  statistics import mean,stdev,variance
```

* Scipy. http://www.scipy.org/
  
* numpy. http://www.numpy.org/
  
* matplotlib.  http://matplotlib.org/

* Lectures on scientific computing with python https://github.com/jrjohansson/scientific-python-lectures


 
