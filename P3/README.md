
## Practice 3(10)

**C/C++ Programming**： GCC and Make, the Shared Library, Sorting Algorithms

Deadline: 2021.06.11

## 要求：

基于[bubble sort及其速度测试示例](./demo_p3/) 和 排序算法 `UnitDS-3-Sorting_Algorithms.ipynb`, 进行以下工作：

将merge sort、insert sort和quick sort排序算法加入示例工程，使用`10000`到`50000`范围中的多组数据集测试不同排序算法的计算速度

基于算法原理和速度测试，给出分析文档

1. 排序算法，速度测试源码及编译makefile文件(4)
   
   * 排序算法源码
   * 排序算法速度测试源码
   * 编译生成速度测试程序的makefile文件：makefile
  
2. 生成排序算法Windows动态库的makefile文件(1)
 
   * makedll.mk

3. 生成使用排序算法共享库的速度测试运行程序的makefile文件(1)
 
   * makeclient.mk

4. 练习工作README.md文档(3)：
 
    基于编程和速度测试结果，从以下几个方面进行总结

   * 4种排序算法要点

   * 4种排序算法的时间、空间复杂度和排序稳定性

   * 4种排序算法适用场景

### 注意

例程中有2个使用算法源码/共享库,进行排序速度测试的主程序：

* sortspeed.c 使用单一数据集测试，使用makefile编译运行

* sortspeed_group.c : 多组数据集测试，使用makegroup.mk编译运行
 
可使用其中的任何一个完成练习工作。

`sortspeed_group.c`代码稍复杂，不建议在排序算法源码和共享库实现阶段使用。

在排序算法源码和共享库工作完成后，学有余力的同学可以使用其进行更好的速度比较工作 

### sortspeed_group

编程生成算法测试运行程序

```bash
make -f makegroup.mk
```

运行程序，输出重定向到`./result/speedvalue.csv`文件，然后，使用`plot_speed.py`绘制数据图形

```bash
make -f makegroup.mk run
```
    
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
     │── makeclient.mk: building the speed test executable caller of the shared library of Sorting Algorithms
     │
     |── sortspeed.c the speed test example in C
     |
     |── <img> image used in README.md  
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

   * 补交得分：<=6，截至时间： 2021.06.21

