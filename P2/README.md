## Practice 2(20)

**Object-oriented Programming**：The General Rankine Cycle Simulator 

Apply `computational thinking` to model and solve more complex problems

**Deadline:**  2021.05.24

## Contents and Requirements

Reference [PyRankine](https://github.com/PySEE/PyRankine), design a general energy balance software with Python to analysis the following cycles：

* [Example 8.1：An Ideal Rankine Cycle](./rankine81.md)
* [Example 8.5：A Regenerative Cycle with Open Feedwater Heater](./rankine85.md)
* [Example 8.6：A Reheat–Regenerative Cycle with Two Feedwater Heaters](./rankine86.md)

**SOLUTION**

* The thermal efficiency, %
* Heat Rate,  kJ/kWh
* Steam Rate, kg/kWh

* The specified net power output of the cycle is 100 MW

  * the mass flow rate of the steam,  kg/h

*  The specified mass flow rate of steam entering the first-stage turbine is 150 kg/s

   * the net power, MW

*  The Specified : the net power output or the mass flow rates
   * Turbine power(totalWExtracted), MW
   * Pump power(totalWRequired), MW
   * The rate of heat transfer into the working fluid as it passes through the boiler, (totalQAdded), MW

**注意**：练习不使用Jupyter Notebook；使用Visual Studio Code进行代码设计和文档撰写等工作。

### 数据文件和Python源码(10)

* 节点和设备json数据文件(3)

* Python源码(7)
 
   * 循环中的设备、节点类设计，循环计算实现和输出
 
### 软件设计工作Markdown文档(5)

* 设计任务简要描述; 

* 设计方案简要描述
  * 循环分析主流程图  
  * 安装依赖关系计算循环中所有设备的算法流程图
  * 节点、设备类设计
  * 节点和设备类的json描述
  
* 设计工作小结
   
    *  遇到的问题、解决过程 

    *  建议本练习，给出你对下面短文的理解:
 
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

 **文档提示** ：数学公式使用：`LaTex`、流程图使用： [flowchart](https://github.com/adrai/flowchart.js). ( **安装**[Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)插件支持显示)

>* LaTex数学公式: $z=\frac{x}{y}$
>
>* flowchart流程图：
>
>>```flow
>>st=>start
>>e=>end
>>op1=>operation: My Operation
>>st->op1->e
>>```
>
>>![](./img/MarkdownEnhanced.jpg)

## 软件设计提示

通用Rankine Cycle程序的泛化要点:

1.  设备

2.  设备间连接关系

3.  系统能量平衡计算方法

[Example 8.6：A Reheat–Regenerative Cycle with Two Feedwater Heaters](./rankine86.md) 比 `Example8.1，8.5`, 多了不同类型的设备

* reheater, trap

* the closed feedwater heater, the opended feedwater heater with 1 drain water inlet

在理解示例基础上，增加新设备。

**增加新设备的工作**：设备Python类代码； 设备**唯一类型标识字符串**，设备`json描述`

**Results for reference**

* Example 8.1: [rankine81-sp.txt](./rankine81-sp.txt)

* Example 8.5: [rankine85-sp.txt](./rankine85-sp.txt)

* Example 8.6: [rankine86-sp.txt](./rankine86-sp.txt)

## Directories and Files

```txt
 <P2>
   │ 
   |── README.md 设计工作Markdown文档
   |
   |── <img>
   |     |── *.jpg/png  Markdown文档图片
   | 
   |── rankine.py  # main app
   |
   |── <rankinecycle> 
   │    |
   │    |─ *.py
   |
   |── <components> components包
   │    |
   │    |─ *.py
   │   
   |── <data>
        |        
        |──<txtcycle> 循环描述json文件
        │    |
        │    |─ *.json
        │ 
        |── <output> 分析结果文件
             |
             |─ *.txt
``` 

## 提交：

* 电邮： cmh@seu.edu.cn
  * 主题：学号-姓名-2
  * 附件：工作目录压缩文件： **学号-姓名-2.zip**；

* 截至时间：2021.05.24
  * 截至时间后可补交，补交得分<=9. (2021.06.21)

## 参考资源：

* [PySEE/PyRankine](https://github.com/PySEE/PyRankine)

* [Rankine Cycle：OOP](http://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit4-3-RankineCycle-OOP.ipynb)

* [Rankine Cycle：General](http://nbviewer.ipython.org/github/PySEE/home/tree/S2021/notebook/Unit4-4-RankineCycle-General.ipynb)


