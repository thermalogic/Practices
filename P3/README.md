
## Practice 3

**C/C++ Programming**(20)：MinGW-w64(GCC), MakeFile, the Shared Library and ctypes

*  Monte Carlo simulation of finding PI

Deadline: 2020.06.09

## 要求：

学习蒙特卡罗(Monte Carlo)计算圆周率的方法[16_MONTE_CARLO_SIMULATION.ipynb:16.4 Finding π](./16_MONTE_CARLO_SIMULATION.ipynb)，然后。完成以下程序设计任务

**注意：** 此Jupyter Notebook供学习使用，练习不使用Jupyter Notebook形式

1.  蒙特卡罗计算圆周率的方法共享库(8)

    * 蒙特卡罗计算圆周率方法的C/C++语言代码

    * 编译生成算法的共享库（Windows下DLL）的makefile文件

```python  
import random

def variance(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)
    
def stdDev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X)**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    #Counting needles in one quadrant only, so multiply by 4
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        print('Est. = ' + str(round(curEst, 5)) +
          ', Std. dev. = ' + str(round(sDev, 5))
          + ', Needles = ' + str(numNeedles))
        numNeedles *= 2
    return curEst      
```

2. C/C++调用算法共享库的算例(4)

    * 参考[16_MONTE_CARLO_SIMULATION.ipynb](./16_MONTE_CARLO_SIMULATION.ipynb)给出调用算法共享库的C/C++算例程序
    
    * 编译算例程序生成运行文件的makefile文件

```python
estPi(0.01, 100)
```

3. Python语言调用共享库的算例(4)
                  
   * Python语言调用共享库的接口程序
   
   * 使用接口程序，调用共享库的Python算例程序

```python
estPi(0.01, 100)
```
4. 练习工作的README.md文档(4)：

建议内容:
                      
   * 算法说明 
   
   * 程序设计工作简要说明：过程，结果(必须内容：计算机终端中，使用命令编译共享库及算例的`过程`、`结果`截图）

   * 工作小结

###  建议配置VS Code不产生C/C++的缓存预编译头文件
 
VS  Code的C/C++插件默认 `会自动产生预编译头文件`，改进编译、调试性能。但是，其缓存的预编译头文件过大, 小规模项目没有必要使用。

因此，建议配置为 `不产生缓存预编译头文件`。 方法见：[软件安装指导文档的disable precompiled header caching](https://github.com/PySEE/home/blob/S2020/guide/doc/BuildingSoftwareEnvironment.md#d33-disable-precompiled-header-caching) 
 
如果已经产生了建议删除。该预编译头文件的缓存预编译头文件目录当前项目目录的：`.vscode/ipch`。注意： `.vscode/`是隐藏目录，需开启 `“文件资源管理器”`的  `“显示隐藏的项目”`

## Directories and Files

```txt
 
|── <P3>
     │ 
     │── README.md: intro of your works(display the screenshots of coding,making and running)
     | 
     │── makefile: building the executable file with source code of MONTE CARLO π
     │ 
     │── makefile-dll.mk: building the shared library of MONTE CARLO π
     │               
     │── makefile-exe.mk: building the executable file with the shared library of MONTE CARLO π
     │
     |── <img>: screenshots of coding,building and running
     |       │
     |       |── *.jpg/png 
     |
     |── <bin>:
     |       │
     |       |── *.exe
     |       |     
     |       |── *.dll
     |
     |── <src>: 
     |        │
     |        |──*.c/cpp, *.h     
     |
     |
     |── <python>: 
             │
             |──*.py                       
```  

## 提交：

压缩工作目录为文件 ：**学号-姓名-3.zip**

* 电邮到：cmh@seu.edu.cn 
    
  * 主题：学号-姓名-3
    
  * 附件：**学号-姓名-3.zip**

* 截至时间：2020.06.09

   * 补交得分：<=13，截至时间： 2020.06.14

## Reference

* [GCC: MAKE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit7-1-GCC_MAKE.ipynb)

* [C: stdio](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit7-2-C_stdio.ipynb)

* [GCC: Lib](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-1-GCC_Lib.ipynb)

* [ctypes](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit8-2-ctypes.ipynb)