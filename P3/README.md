## Practice 3

**Object-oriented Programming**(20)：The General Rankine Cycle Simulator 

**注意：** 如果使用csv文件格式配置循环数据的程序实现困难，可以参考[PyRankine](https://github.com/PySEE/PyRankine)新增的使用json文件格式配置循环数据的程序。json文件格式可读性更好些。
  
### Purpose

The Rankine Cycle Simulator: training computational thinking and  programming skills  

Apply **abstraction** and **decomposition** to solve more complex problems

* Can decompose a large problem into parts and design algorithms to solve them
* Can recognise similar problems, and apply generic solutions and abstractions
* Can effectively combine functionality from multiple libraries or APIs and refer to documentation
* Can write code in a readable way, and/or includes comments where necessary

**Deadline:**  2018.05.15

## The Rankine Cycle: 

Michael J . Mora. Fundamentals of Engineering Thermodynamics (7th Edition).  John Wiley & Sons, Inc. 2011

(Please search web to download the PDF,e.g http://muchong.com/html/201501/8475071.html or  http://ishare.iask.sina.com.cn/f/34258437.html )

Chapter 8 Vapor Power System: 

* Example 8.1：An Ideal Regenerative Cycle, Page 438

* Example 8.5: A Regenerative Cycle with Open Feedwater Heater,Page 456

* Example 8.6 : Considering a Reheat–Regenerative Cycle with Two Feedwater Heaters, a closed feedwater heater and an open feedwater heater,Page 460


## 要求：(总分20)

通用Rankine Cycle计算程序设计：能够解析数据文件描述的循环系统拓扑结构，读取热力参数，计算出循环的各项数据，并将结果输出到数据文件

计算对象：[Example 8.1](./rankine81.md)、[Example 8.5](./rankine85.md)、[Example 8.6](./rankine86.md)  

计算结果：[rankine81-SP.txt](./rankine81-SP.txt)、[rankine85-SP.txt](./rankine85-SP.txt)、[rankine86-SP.txt](./rankine86-SP.txt)

设计提示：[tips](./tips.md)

编码工具：Visual Studio Code
     
Python3代码(15)：

   * 使用类描述循环中的设备(组件)、循环,实现计算目标(10)

   * 使用数据文件描述被计算循环的拓扑结构和热力参数 (2)

 >**注意：** PyRankine示例的实现方案中：csv格式的设备数据文件中每个设备最后的项目是节点：　NODES,,,,,,
 >
 > 节点内容需要和相应设备类的｀__init__｀方法中定义的节点数量和顺序对应。
 > 
 >可为建立设备数据文件中每个设备的节点要求，根据｀__init__｀方法写一个文档，用于指导建立设备数据文件时的NODES,,,,,,数据配置  
      
   * 计算结果输出到数据文件(3)
    
文档(5)：软件设计思路和体会（关键问题、解决方案；设备对象的定义、循环计算方法，小结）的Markdown文档（中英文皆可）

>**注意：** 这个练习不使用Jupyter Notebook的形式. Python代码和文档分离

## 提交：

* 1 电邮： cmh@seu.edu.cn
   * 主题：学号-姓名-3
   * 附件：程序文件压缩包： **学号-姓名-3.zip**；

* 2 截至时间：2018.05.15
   * 过截至时间后可补交，补交得分<=13. (2018.06.15)

* 3)改进更新：提交作业后可改进，改进截至时间：2018.06.15

## 参考资源：

*  http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/PyThermo-IdealRankineCycle.ipynb
 
*  https://github.com/PySEE/PyRankine Step3, Step4

*  curriculum.raspberrypi:developer https://curriculum.raspberrypi.org/programming/developer/
