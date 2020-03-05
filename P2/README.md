## Practice 2(20)

**Object-oriented Programming**：The General Rankine Cycle Simulator 

Apply `computational thinking` to model and solve more complex problems

**Deadline:**  2020.05.19

## Contents and Requirements

Reference [PyRankine](https://github.com/PySEE/PyRankine), design a general energy balance software with Python to analysis the following cycles:

* [Example 8.1：An Ideal Regenerative Cycle](./rankine81.md)

* [Example 8.5：A Regenerative Cycle with Open Feedwater Heater](./rankine85.md)
 
* [Example 8.6：A Reheat–Regenerative Cycle with Two Feedwater Heaters](./rankine86.md) 

**注意**：练习不使用Jupyter Notebook；使用Visual Studio Code进行代码设计等工作，使用MS Word编写设计文档。

### 数据文件和Python3源码(12)

* 数据文件：建立描述循环系统和设备的json文件(2)

* Python3源码
 
   * 使用类描述循环中的设备(组件)、节点(5)

   * 编程读取系统描述json文件，解析其描述的循环系统，进行循环的能量平衡分析(4)

* 数据文件：输出分析结果到数据文件(1)
  
### 软件设计工作Word文档(8)

* 设计问题简要描述(1); 

* 程序设计方案简要描述(5)
  * 总体思路；   
  * 系统json文件描述；
  * 节点和设备类的设计；
  * 循环能量平衡计算过程；

* 设计工作小结(1)

    小结中，建议结合练习，给出你对下面短文的理解:
 
  >Programming is about managing complexity in a way that facilitates change. There are two powerful mechanisms available for accomplishing this: decomposition and abstraction`
  > 
  >Apply `abstraction` and `decomposition` to model and solve more complex problems
  >
  > * decompose a large problem into parts and design algorithms to solve them
  >
  > * recognise similar problems, and apply generic solutions and abstractions
  >
  > * creating algorithms to obtain the generic solution results
  >
  > The set of problem-solving methods with computer is also called **Computational Thinking**. 
  
 
* Word排版(1): 版面整洁，合理划分和组织文档段落；页眉：练习二 学号 姓名； 页脚：页码 

  * **无需** 封面和目录

## 提示

[Example 8.6：A Reheat–Regenerative Cycle with Two Feedwater Heaters](./rankine86.md) 比 `Example8.1，8.5`, 多了不同类型的设备

* reheater, trap

* the closed feedwater heater, the opended feedwater heater with 1 drain water inlet

需要在理解示例基础上，增加新设备。

增加新设备的工作： 首先，需要规定好新设备的**唯一类型标识字符串**，然后，是设备的json描述，计算分析Python类实现及相关代码工作，实现更通用的循环计算程序。

通用Rankine Cycle程序的泛化要点:

1.  设备

2.  设备间连接关系

3.  系统能量平衡计算方法

**Results for reference**

* Example 8.1: [rankine81-sp.txt](./rankine81-sp.txt)

* Example 8.5: [rankine85-sp.txt](./rankine85-sp.txt)

* Example 8.6: [rankine86-sp.txt](./rankine86-sp.txt)

## Directories and Files

```bash
 ├──<Practices>
     │ 
     |── <P2>
          │ 
          |── *.docx 设计工作Word文档
          |
          |── *.py  循环分析Python源码文件
          |
          |── <components> components包的源码文件
          │    |
          │    │ ── *.py
          │   
          |── <txtcycle> 各循环描述json文件
          │    |
          │    │ ── *.json
          │ 
          |── <output> 各循环分析结果文件
               |
               │ ── *.txt
``` 

## 提交：

* 电邮： cmh@seu.edu.cn
  * 主题：学号-姓名-2
  * 附件：工作目录压缩文件： **学号-姓名-2.zip**；

* 截至时间：2020.05.19
  * 截至时间后可补交，补交得分<=13. (2020.06.14)

## 参考资源：

* [PySEE/PyRankine](https://github.com/PySEE/PyRankine)

* [Rankine Cycle：OOP](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-3-RankineCycle-OOP.ipynb)

* [Rankine Cycle：General](http://nbviewer.ipython.org/github/PySEE/home/tree/S2020/notebook/Unit4-4-RankineCycle-General.ipynb)


