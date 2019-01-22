## Practice 3(20)

**Object-oriented Programming**：The General Rankine Cycle Simulator 

Apply computational thinking to solve more complex problems

**Deadline:**  2019.05.19


>练习的工作量和难度都较大。同学们，多思考，多编码，尽自己的能力进行程序设计工作。从学习角度来讲，**程序设计的过程，比结果重要！**
   

## 分析对象

Michael J . Moran. Fundamentals of Engineering Thermodynamics (7th Edition).  John Wiley & Sons, Inc. 2011/(8th Edition) 2015

Please download the ebook from SEU: http://www.lib.seu.edu.cn/ （查找资源->外文电子书->Wiley电子教材->T(工业技术)->TK(能源与动力工程)->TK1(热力工程,热机)）

Chapter 8 Vapor Power System(7th Edition): 

* [Example 8.1](./rankine81.md)：An Ideal Regenerative Cycle, Page 438

   * [Jupyter Notebook of Example 8.1 @PySEE/PyRankine](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle81-82-Step0-1.ipynb) 

* [Example 8.5](./rankine85.md): A Regenerative Cycle with Open Feedwater Heater,Page 456

   * [Jupyter Notebook of Example 8.5 @PySEE/PyRankine](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle85-Step0.ipynb) 

* [Example 8.6](./rankine86.md) : A Reheat–Regenerative Cycle with Two Feedwater Heaters, a closed feedwater heater and an open feedwater heater,Page 460

   * [Jupyter Notebook of Example 8.6 @PySEE/PyRankine](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle86-Step0.ipynb) 

参考结果：

* Example 8.1: [rankine81-SP.txt](./rankine81-SP.txt)

* Example 8.5: [rankine85-SP.txt](./rankine85-SP.txt)

* Example 8.6: [rankine86-SP.txt](./rankine86-SP.txt)

## 工作内容和要求(20)

参考[PyRankine](https://github.com/PySEE/PyRankine), 以Michael J . Moran热力学教程中的[Example 8.1](./rankine81.md)，[Example 8.5](./rankine85.md)，[Example 8.6](./rankine86.md)为分析对象，进行通用Rankine Cycle能量平衡程序设计。

* 建立循环系统和设备的数据文件

* 编程实现，读取数据文件，解析其描述的循环系统拓扑结构，计算热力参数，给出循环系统的各项指标

* 输出结果到数据文件。

**数据文件和Python3源码(15)：**

   * 使用类描述循环中的设备(组件)、节点(6)

   * 循环描述数据文件(拓扑结构、设备数据)(3)
   
   * 解析描述循环系统的数据文件，计算热力参数,计算循环的各项指标(4)

   * 计算结果输出到数据文件(2)
  
**Word文档(5)**：问题描述; 求解思路；系统的数据文件表达方案；设备组件，节点对象设计；循环计算方法实现等；设计经验，体会等工作小结）

   * 文档格式： 1) 版面整洁，合理划分和组织文档段落；2) 页眉：练习三 学号 姓名； 3) 页脚：页码；4)**无需**封面和目录

**注意**：这个练习不使用Jupyter Notebook；使用Visual Studio Code进行代码设计等工作。

## 提示

### 设备类的实现

Example8.6是再热-回热循环Rankine循环，比示例Example8.1，8.5多了不同类型的设备(reheater,the closed feedwater heater)，需要在理解示例代码基础上，增加新设备类代码，进而实现更通用的循环计算程序。此外，可参考 [TIPS](./tips.md)。

### 循环描述数据文件

PyRankine Step3~5 使用了`csv`和`json`两种格式的系统描述数据文件实例，根据自己的理解选择一种数据文件格式，进行程序设计工作。

#### csv格式

系统描述数据文件中每个设备行的最后一项目是节点：　`NODES,,,,,,`

数据文件中节点内容需要和相应设备类的 `__init__` 方法中定义的节点数量和顺序对应。
 
可根据每个设备的 `__init__` 方法写一个文档，用于指导建立相应设备数据文件时的`NODES,,,,,,`数据配置要求  

#### json格式 

数据结构性好,需学习json相关知识。

* [PyThermo-RankineCycle-CSV-JSON-UML](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-2-PyThermo-RankineCycle-CSV-JSON-UML.ipynb)
 
* [PyThermo-JSON-Python](https://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-3-PyThermo-JSON-Python.ipynb)

## 提交：

* 1 电邮： cmh@seu.edu.cn
   * 主题：学号-姓名-3
   * 附件：程序文件压缩包： **学号-姓名-3.zip**；

* 2 截至时间：2019.05.19
   * 截至时间后可补交，补交得分<=13. (2019.06.16)

* 3 改进更新：提交作业后可修改，修改截至时间：2019.06.16

## 参考资源：

* [PySEE/PyRankine Step2~5](https://github.com/PySEE/PyRankine)

* [Jupyter Notebook of Example 8.1~8.6  @PySEE/PyRankine](https://github.com/PySEE/PyRankine/tree/master/notebook)

* [PyThermo-IdealRankineCycle-OOP](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-1-PyThermo-IdealRankineCycle-OOP.ipynb)

* [PyThermo-RankineCycle-CSV-JSON-UML](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-2-PyThermo-RankineCycle-CSV-JSON-UML.ipynb)

* [PyThermo-JSON-Python](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit4-3-PyThermo-JSON-Python.ipynb)