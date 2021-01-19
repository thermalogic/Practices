
## Practice 3(10)

**C/C++ Programming**： GCC on Windows, Make, the Shared Library and ctypes

*  Monte Carlo simulation of finding PI

Deadline: 2021.06.11

## 要求：

学习蒙特卡罗(Monte Carlo)计算圆周率的方法[MONTE CARLO SIMULATION:16.4 Finding π](./16_MONTE_CARLO_SIMULATION.ipynb)，完成以下程序设计任务

**注意：** 此Jupyter Notebook供学习算法使用，练习不使用Jupyter Notebook形式

1.  蒙特卡罗计算圆周率的方法共享库(5)

    * 蒙特卡罗计算圆周率方法的C语言代码

    * 编译生成算法共享库(使用`__cdecl`约定，Windows下DLL)的makefile文件

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
        numNeedles *= 2
    return curEst      
```

2. 调用算法共享库的算例(3)

    * C语言调用共享库算例源码及编译生成运行文件的makefile文件(2)

    * Python语言调用共享库的接口及其使用算例(1)

3. 练习工作的README.md文档(2)：

建议内容:
                      
   * 算法说明 
   
   * 程序设计工作简要说明：过程，结果(文字和截图）
    
     * 必含内容：在终端中编译共享库及算例的 **工作过程和结果的截图**

   * 工作小结

###  VS Code配置建议

建议配置VS Code不产生C/C++的缓存预编译头文件
 
VS Code的C/C++插件默认 `自动产生预编译头文件`，用于改进编译、调试性能, 但是，其缓存的预编译头文件过大(The defualt Cache Size is 5120 MB), 小规模项目没有必要使用。

建议配置为 `不产生缓存预编译头文件`, 方法如下：

* set the `"C_Cpp.intelliSenseCacheSize:"0` to disable Precompiled header caching   

   ![vscode_pch_cache](./img/vscode_pch_cache.jpg)
 
如果已经产生了, 建议删除:

* 该预编译缓存头文件位于当前项目目录的：`.vscode/ipch`。注意： `.vscode/`是隐藏目录，需开启 `“文件资源管理器”`的  `“显示隐藏的项目”`

## Directories and Files

```txt
 
|── <P3>
     │ 
     │── README.md: intro of your works(display the screenshots of coding,making and running)
     | 
     │── makefile: building the executable file with source code of MONTE CARLO π
     │ 
     │── makedll.mk: building the shared library of MONTE CARLO π
     │               
     │── makeexe.mk: building the executable caller of the shared library of MONTE CARLO π
     │
     |── demo.c the example in C
     │
     |── example.py the example in Python
     │
     |── <img> screenshots of coding,building and running
     |       │
     |       |── *.jpg/png 
     |
     |── <bin>
     |       │
     |       |── *.exe
     |       |     
     |       |── *.dll
     |
     |── <include> 
     |        │
     |        |──*.h     
     |── <src> 
     |        │
     |        |──*.c     
     |
     |── <python> 
             │
             |──*.py  the API in Python                     
```  

## 提交：

压缩工作目录为文件 ：**学号-姓名-3.zip**

* 电邮到：cmh@seu.edu.cn 
    
  * 主题：学号-姓名-3
    
  * 附件：**学号-姓名-3.zip**

* 截至时间：2021.06.11

   * 补交得分：<=9，截至时间： 2021.06.21

