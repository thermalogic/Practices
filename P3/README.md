
## Practice 3(8)

**C/C++ Programming**： GCC and Make, the Shared Library, Sorting Algorithms

Deadline: 2023.06.10

## 要求：

基于[排序算法速度测试示例](./demo_p3/), 编写 `选择排序` 和 `归并排序` 算法速度测试代码，并给出算法原理文档

1. 排序算法、速度测试源码(2)
   
   * 加入 `归并排序`的C语言实现
  
2. 编译生成速度测试程序的makefile文件：makefile(1)
  
3. 生成排序算法Windows动态库的makefile文件(1)
 
   * makedll.mk

4. 生成使用排序算法共享库的速度测试运行程序的makefile文件(1)
 
   * makeclient.mk

5. 练习工作README.md文档(3)：
 
   * 2种排序算法要点

   * 2种排序算法的时间、空间复杂度和排序稳定性

### sort_speed

编程生成算法测试运行程序

```bash
make
```

运行程序，输出重定向到`./result/speed_value.csv`文件，然后，使用`plot_speed.py`绘制数据图形

```bash
make run
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
 
<学号-姓名-3>
     │ 
     │── README.md: doc of your works
     | 
     │── makefile: building the speed test executable file with source code of Sorting Algorithms
     │ 
     │── makedll.mk: building the shared library of Sorting Algorithms
     │               
     │── makeclient.mk: building the speed test executable caller of the shared library 
     │
     |── sort_speed.c ：the speed test code
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
              │
              |──*.c     
      
                         
```  
