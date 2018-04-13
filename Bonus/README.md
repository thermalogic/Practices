# Bonus(+5) 

Programming with GCC,Ubuntu

Deadline: 2018.06.12
 
## 1 C/C++ Programming with MinGW-w64(+3) 

Using MinGW-w64(GCC and make) under Windows

* The code of  the shared library of IF97-Region4 **Eq. (30)** and makefile

* The example codes of using the shared library of IF97-Region4 **Eq. (30)**  and makefile

IF97-Rev.pdf  http://www.iapws.org/relguide/IF97-Rev.pdf

 * 8.1 The Saturation-Pressure Equation (Basic Equation)  **Eq. (30)**

**Reference**

* [CPP_1_GCC_DLL](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/CPP_1_GCC_DLL.ipynb)

* [CPP_2_DLL_Python_VBA](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/CPP_2_DLL_Python_VBA.ipynb)

## 2 Programming under Ubuntu(+2)   

C/C++ Programming with `GCC and make`,`GSL and GNUPlot` 

* Using **GSL** to do Linear Regression of Springs Behavior Data [springData.csv](springData.csv)

* Using **Gnuplot** to visualize the  data and Linear Regression results 

![Linear Regression of Springs Behavior](spring.jpg)

**NOTE：** you may using "Windows Subsystem for Linux": https://docs.microsoft.com/zh-cn/windows/wsl/install-win10

if so, you may change sources to china as the following steps:

1. backup 

```bash
cp /etc/apt/sources.list /etc/apt/sources.list_backup
```
2. change to the sources to aliyun through `vim` 

```bash
$vim /etc/apt/sources.list
```

```
:%s#deb http://archive.ubuntu.com/ubuntu/#deb http://mirrors.aliyun.com/ubuntu/#g
:%s#deb http://security.ubuntu.com/ubuntu/#deb http://mirrors.aliyun.com/ubuntu/#g
```

3. update
```bash
$apt-get update
```
**Reference**

* [15_UNDERSTANDING_EXPERIMENTAL_DATA](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/15_UNDERSTANDING_EXPERIMENTAL_DATA.ipynb)

* [SUPL-2-GSL-GNUPLOT-Ubuntu](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/SUPL-2-GSL-GNUPLOT-Ubuntu.ipynb)

## 提交：

* 1 电邮：cmh@seu.edu.cn

   * 主题：学号-姓名-B
  
   * 附件：学号-姓名-B.zip

* 2 **截至时间**：2018.06.12

## Reference

* GSL - GNU Scientific Library https://www.gnu.org/software/gsl/

* The GSL Reference Manual online https://www.gnu.org/software/gsl/doc/html/index.html

* Gnuplot homepage http://gnuplot.info/

* Nishanth Sastry：gnuplot 让您的数据可视化 https://www.ibm.com/developerworks/cn/linux/l-gnuplot/