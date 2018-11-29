
## Practice 5

**C/C++ Programming**(5)：C/C++ Programming with MinGW-w64（GCC,Make),Visual Studio Code 

Deadline: 2019.06.09

## Task(5分)：

The exponentiating by squaring is a general method for fast computation of large positive integer powers of a number.

https://en.wikipedia.org/wiki/Exponentiation_by_squaring

Please use the [fastipow.cpp](./src/fastipow.cpp) to program the following tasks:

* Source files(C/C++ code/header):(1.5)

    *  The function of The Repeated Squaring Method

    *  The example application to call The Repeated Squaring Method

* Makefiles(3)

    * Making the executable file with multiple source files: the function of The Repeated Squaring Method and it's caller

    * Making the shared library of the Repeated Squaring Method

    * Making the executable file to call the shared library 

* Images：(0.5)

     * The screenshot of coding,making exe to use the shared library and running the exe
   
     Example:

   ![screenshots](./img/vscode-gcc.jpg)


```bash
 ├──<Practices>
 │   │ 
 │   |── <P5>
 │   │    │ 
 │   │    |── <img>: screenshots of coding,making and running
 │   │    │ 
 │   │    |── <bin>: *.exe, *.dll
 │   │    |
 │   │    |── <src>: *.c,*.cpp, *.h
 │   │    |
 │   │    │── makefile:  building exe with multi-source files: the function code and it's caller code
 │   │    │ 
 │   │    │── makefile-dll:  building the shared library 
 │   │    │               
 │   │    │── makefile-exe: building exe to use the shared library  
 │   │                   
```  

## 提交：

压缩练习目录为zip文件：**学号-姓名-5.zip**

* 1 电邮：cmh@seu.edu.cn 
    
  * 主题：学号-姓名-5
    
  * 附件：程序文件压缩包：**学号-姓名-5.zip**

* 2 截至时间：2019.06.09

   * 截至时间后可补交， 得分<=3 (2019.06.16 )

* 3 改进更新：提交作业后可改进，改进截至时间：2019.06.16

## Reference

* [GCC_MAKE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-1-GCC_MAKE.ipynb)

* [GCC_DLL](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-2-GCC_DLL.ipynb)

