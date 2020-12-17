## Practice 2(15)

**Object-oriented Programming**：The  vapor-compression refrigeration  cycle simulator 

Apply `computational thinking` to model and solve the industrial process problems

**Deadline:**  2021.05.24

## Contents and Requirements

以[PySimVCR](https://github.com/PySEE/PySimVCR)为基础，编写代码，使其可计算如下2个循环：

* Thuan Ke Nguyen, [CHE 302 Chemical and Materials Engineering Thermodynamics I: chap7-2](https://www.cpp.edu/~tknguyen/che302/Notes/chap7-2.pdf)

### 1. Example 7.2-5 Page4 

Refrigerant 134a is the working fluid in the vapor-compression refrigeration cycle that communicates thermally with

* a cold region at -10°C 

* Saturated vapor enters the compressor at -10°C 

* liquid leaves the condenser at 0.9MPa and 30°C 

* The compressor has **an efficiency of 80%** 

* The mass flow rate of the refrigerant is 0.08kg/s 

**Determine**

 * the compressor power, in kW
 
 * the refrigeration capacity, in tons
 
 * the coefficient of performance

### 2 Modified Example 7.2-5 Page4 

Refrigerant 134a is the working fluid in the vapor-compression refrigeration cycle that communicates thermally with

* a cold region at -10°C 

* Saturated vapor enters the compressor at -10°C and **Superheated vapor leaves the compressor at 50°C** 

* liquid leaves the condenser at 0.9MPa and 30°C

* The mass flow rate of the refrigerant is 0.08kg/s

**Determine**

* **the efficiency of compressor, in %** 

* the compressor power, in kW
 
* the refrigeration capacity, in tons
 
* the coefficient of performance

 ![](img/example725.jpg) 

### 练习提示

[PySimVCR](https://github.com/PySEE/PySimVCR)示例中压缩机类的压缩过程是等熵过程，练习中需计算的循环不是等熵过程。

程序需要能够处理：等熵过程、不同已知参数的不可逆非等熵过程，因此，练习需做以下编码工作：

1. compressor压缩机类模块修改：属性、计算及输出

   * 循环Example 7.2-5：已知压缩机效率
 
   * 修改了已知参数的循环Example 7.2-5：已知压缩机出口温度，计算压缩机效率

2. 循环数据Python模块

   * 修改数据模块节点和设备字典定义, 适应不同的已知参数

3. 其他修改和完善

**建议工作步骤**，

* 首先，分析 **循环Example 7.2-5**，修改代码，实现其计算

* 进一步，分析 **修改了已知参数的循环Example 7.2-5**，修改代码，实现可以计算不同类型和参数条件循环的分析软件

### Python源码(8)

* 循环数据Python模块(3)

* 设备类(5)
 
### 软件设计工作Markdown文档(7)

* 设计任务简要描述;

* 设计方案简要描述
  * 循环分析流程图  
  * 节点、设备类
  * 循环数据Python模块
  
* 设计工作小结
   
    *  练习中遇到的问题及其解决过程 

    *  对编程思维理解
    
    *  对工业软件的思考
  
 **文档提示** ：数学公式可使用：`LaTex` (**需**[Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)插件支持显示)

>* LaTex数学公式: $z=\frac{x}{y}$

## 提交：

* 电邮： cmh@seu.edu.cn
  * 主题：学号-姓名-2
  * 附件：工作目录压缩文件： **学号-姓名-2.zip**；

* 截至时间：2021.05.24
  * 截至时间后可补交，补交得分<=9. (2021.06.21)


