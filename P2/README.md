## Practice 2(15)

**Python and Interactive Computing**：The Simple Simulator of Rankine Cycle 

Deadline: 2019.04.21

## Goal

Use **Jupyter Notebook** to simulate the Rankine Cycle 

* interactive analysis and literate programming

* abstracte the items in the problem with the structure types

* review the knowledge of Rankine Cycle

## The Rankine Cycle 

Michael J. Moran. Fundamentals of Engineering Thermodynamics (7th Edition).  John Wiley & Sons, Inc. 2011

Chapter 8 Vapor Power System:(Page 460-463)

[Example 8.6](./rankine86.md): Considering a Reheat–Regenerative Cycle with Two Feedwater Heaters, a closed feedwater heater and an open feedwater heater. 

* [Jupyter Notebook of Example 8.6](https://github.com/PySEE/Practices/tree/S2019/P2/RankineCycle86.ipynb) 
  
* [Solution of Example 8.6](./rankine86-SP.txt)

## 要求：(15)

Example 8.6热力循环计算的Jupyter Notebook
    
**代码部分**(10)：
  
  * 使用结构数据类型：**列表、字典**等描述循环中的状态点，设备和循环性能指标(4)

  * 基于数据结构的设计，使用**函数**封装计算模块，组织循环计算(3)

  * 全面清晰输出：循环参数和性能指标等计算结果(3)
  
  
**文档部分**(5);   
    
* 格式：原则上采用Markdown，如果需特殊效果，可少量使用HTML; 公式用Mathjax; 中英文皆可。

* 内容：

  * 问题描述(1)
        
  * 设计思路(2)
        
  * 模块说明(1)
        
  * 小结(1) 
> **注意：** 需要合理组织Notebook中文档和代码的顺序，如：先交待被计算对象，然后，设计思路，进一步是文档和相关代码，最后，小结 。

**参考设计:**
       
  * PyRankine https://github.com/PySEE/PyRankine  step0, step1

  * [Jupyter Notebook of IdealRankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-2-PyThermo-IdealRankineCycle.ipynb)

  * [Jupyter Notebook of Example 8.6](https://github.com/PySEE/Practices/tree/S2019/P2/RankineCycle86.ipynb) 
  
    **Note: you may use the Notebook to start the practice** 
     
## 提交：

* 1 电邮： cmh@seu.edu.cn
   
  * 主题：学号-姓名-2
  * 附件：Jupyter Notebook等文件的压缩包： **学号-姓名-2.zip**；

* 2 **截至时间：** 2019.04.21
  
  * 截至时间后补交，补交得分<10. (2019.06.16)

* 3 改进更新：提交作业后可改进，改进截至时间：2019.06.16

## 参考资源：

* [Markdown](https://github.com/PySEE/home/blob/S2019/guide/Introduction2Markdown.md)

* [MathJax LaTeX](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-3-Thermo-MathJax-LaTeX.ipynb)

* Jupyter Documentation. http://jupyter.readthedocs.org/en/latest/
    
    * IPython https://ipython.org/
    
    * A gallery of interesting notebook：https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

* [PyThermo-IF97](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-1-PyThermo-IF97.ipynb)

* [Jupyter Notebook of IdealRankine Cycle](http://nbviewer.ipython.org/github/PySEE/home/tree/S2019/notebook/Unit2-2-PyThermo-IdealRankineCycle.ipynb) 

*  PyRankine https://github.com/PySEE/PyRankine

     * step 0 : **Zero Abstraction** :  the simple data type and expression only 

     * step 1 : **Simple Abstraction** : structure data type: List,Dict and functions

*  Michael J . Moran. [Chapter 8's Jupyter Notebook for Fundamentals of Engineering Thermodynamics](https://github.com/FOSSEE/Python-Textbook-Companions/blob/master/Fundamental_of_Thermodynamics_by_Moran_and_Shapiro_by_Michael_J._Moran_and_Howard_N._Shapiro/Chapter_8.ipynb)




  

