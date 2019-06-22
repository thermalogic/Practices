
## Practice 4

**C/C++ Programming**(15)：C/C++ Programming with MinGW-w64（GCC)，MakeFile,the Shared Library

Deadline: 

## 要求：

1 实现MIT书中的蒙特卡罗方法计算Pi的C语言共享库 -使用makefile
               
2 给出C/C++调用共享库的算例（不同needle的计算）- 使用makefile
                  
3 给出Python语言调用共享库的算例，和纯Python语言实现蒙特卡罗方法比较计算速度timeit
                  
4 撰写练习的README.md文档：
                      
   算法说明  程序设计工作简要说明    终端中编译，运行过程及结果输出截图1

## Directories and Files

```txt
 
|── <P4>
     │ 
     │── README.md: intro of your works(display the screenshots of coding,making and running)
     | 
     │── makefile:  building the executable file with multiple source     
     │ 
     │── makefile-dll: building the shared library 
     │               
     │── makefile-exe: building the executable file to call the shared library  
     │
     |── <img>: screenshots of coding,making and running
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
             │
             |──*.c/cpp, *.h                   
```  

## 提交：

Compress your practice folder to ：**StudentNumber-Name-4.zip**

     注意压缩工作目录时，删除`C/C++ for Visual Studio Code`产生的缓存预编译头文件目录：.vscode/ipch
     
     .vscode/是隐藏目录，需开启“文件资源管理器”的显示“隐藏的项目”

* 1 Email to：cmh@seu.edu.cn 
    
  * Subject：StudentNumber-Name-4
    
  * Attachment：**StudentNumber-Name-5.zip**

* 2 Deadline：

   * make up after deadline: points<=9 

* 3 Improvement: due：

## Reference

* [GCC_MAKE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-1-GCC_MAKE.ipynb)

* [GCC_DLL](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit8-2-GCC_DLL.ipynb)

