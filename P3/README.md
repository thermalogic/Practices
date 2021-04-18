
## Practice 3(10)

**C/C++ Programming**： GCC and Make, the Shared Library, Sorting Algorithms

Deadline: 2021.06.11

## 要求：

基于[bubblesort及其速度测试示例](./demo_p3/)，完成以下工作

1. 学习排序算法`UnitDS-3-Sorting_Algorithms.ipynb`, 然后，将mergesort、insertsort和quicksort排序算法加入示例工程，使用`10000、50000, 100000`数据集测试不同排序算法的计算速度(4)
 
   * 排序算法源码
   * 排序算法速度测试源码
   * 编译生成测试速度程序的makefile文件：makefile
  
3. 排序算法共享库(1)

   * 编译生成算法共享库(`__cdecl`约定，Windows下DLL)的makefile文件： makedll.mk

4. 调用排序算法共享库(1)

    * C语言调用排序算法及编译生成运行文件的makefile文件： makeexe.mk

5. 练习工作README.md文档(4)：结合算法编程和速度测试实践，对排序算法进行分析和总结

   * 4种排序算法要点

   * 4种排序算法的时间、空间复杂度和排序稳定性

   * 4种排序算法适用场景
    
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
     │── README.md: doc of your works
     | 
     │── makefile: building the speed test executable file with source code of Sorting Algorithms
     │ 
     │── makedll.mk: building the shared library of Sorting Algorithms
     │               
     │── makeexe.mk: building the speed test executable caller of the shared library of Sorting Algorithms
     │
     |── sortspeed.c the speed test example in C
     |
     |── <img> image used in README.md  │
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
                         
```  

## 提交：

压缩工作目录为文件 ：**学号-姓名-3.zip**

* 电邮到：cmh@seu.edu.cn 
    
  * 主题：学号-姓名-3
    
  * 附件：**学号-姓名-3.zip**

* 截至时间：2021.06.11

   * 补交得分：<=9，截至时间： 2021.06.21

