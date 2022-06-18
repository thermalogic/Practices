## Practice 1

**Data Analysis**(10)：Statistics, regression and visualization

* Deadline: 2023.04.29

## Problem

John V. Guttag. Introduction to Computation and Programming Using Python: With Application to Understanding Data(third Edition). MIT Press, 2021. 

**22.5 Statistical Measures Don't, Tell the Whole Story**(Page521-522) 
  
In 1973, the statistician F.J. Anscombe published a paper containing the table below. It contains the <x, y> coordinates of the points in each of four data sets.

| x    |   y   |   x   |   y   |   x   |   y   |   x   |    y |
| ---- | :---: | :---: | :---: | :---: | :---: | :---: | ---: |
| 10.0 | 8.04  | 10.0  | 9.14  | 10.0  | 7.46  |  8.0  | 6.58 |
| 8.0  | 6.95  |  8.0  | 8.14  |  8.0  | 6.77  |  8.0  | 5.76 |
| 13.0 | 7.58  | 13.0  | 8.74  | 13.0  | 12.74 |  8.0  | 7.71 |
| 9.0  | 8.81  |  9.0  | 8.77  |  9.0  | 7.11  |  8.0  | 8.84 |
| 11.0 | 8.33  | 11.0  | 9.26  | 11.0  | 7.81  |  8.0  | 8.47 |
| 14.0 | 9.96  | 14.0  | 8.10  | 14.0  | 8.84  |  8.0  | 7.04 |
| 6.0  | 7.24  |  6.0  | 6.13  |  6.0  | 6.08  |  8.0  | 5.25 |
| 4.0  | 4.26  |  4.0  | 3.10  |  4.0  | 5.39  | 19.0  | 12.5 |
| 12.0 | 10.84 | 12.0  | 9.13  | 12.0  | 8.15  |  8.0  | 5.56 |
| 7.0  | 4.82  |  7.0  | 7.26  |  7.0  | 6.42  |  8.0  | 7.91 |
| 5.0  | 5.68  |  5.0  | 4.74  |  5.0  | 5.73  |  8.0  | 6.89 |

## 要求(10分)：

实现2种类型的数据分析软件:  Python脚本、Jupyter Notebook 

* 1 读取数据文件(2分) [./data/anscombe.csv](./data/anscombe.csv)，使用List,Dict表达数据(自编码,不使用软件包)
 
* 2 统计指标计算和输出(3分)：
    * 计算均值、方差和相关系数统计指标 (2分， 自编码，不使用软件包)
    * 使用字符串输出统计结果表格 (1分，自编码，不使用软件包) 

* 3 线性回归和图形输出(3分): 
   * 线性回归  (1分,使用Numpy或Scipy)
   * 图形输出  (2分,使用Matplotlib)

Jupyter Notebook是`文本`+`代码`的交互式文档。在Jupyter Notebook中用文本给出(2分)

* 问题描述

* 软件各部分设计要点和功能说明
 
* 回答问题：如何做一个合格的统计信息消费/生产者 
     * 阅读：`22.5 Statistical Measures Don't, Tell the Whole Story`

### 参考输出

```
─────────────────────────────────────────────────
  No   x-avg  x-pvar  y-avg  y-pvar   pearson_r  
─────────────────────────────────────────────────
  1     9.0    10.0    7.5    3.75     0.816 
  2     9.0    10.0    7.5    3.75     0.816 
  3     9.0    10.0    7.5    3.75     0.816 
  4     9.0    10.0    7.5    3.75     0.817 
─────────────────────────────────────────────────
``` 

![数据点图和回归曲线](./img/anscombe.png)

## 工作目录

```txt
 
 <学号-姓名-1>
     │
     |── 学号-姓名-1.py ：数据分析Python脚本
     |
     │── nb.bat ：启动jupyter服务的批处理文件
     │── 学号-姓名-1.ipynb ：数据分析Jupyter Notebook
     │ 
     |── <data>   
            │
            |── anscombe.csv 数据文件
```

