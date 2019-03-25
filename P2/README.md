## Practice 2(15)

**Python and Interactive Computing**：The Simple Simulator of Rankine Cycle 

Deadline: 2019.04.21

## Goal

Use **Jupyter Notebook** to simulate the Rankine Cycle 

* description of the objects with the structure types，abstraction of procedure with functions 

* interactive analysis and literate programming

## 要求：(15)

设计分析 [Example 8.6：The Reheat–Regenerative Cycle with Two Feedwater Heater](./rankine86.md) 的Jupyter Notebook。

合理组织Notebook中的文档(Markdown Cell)和代码(Code Cell)。如：先给出被计算对象描述，然后，给出总体设计思路，进一步是各部分程序模块说明文字、代码，最后，是设计小结。
    
### Jupyter Notebook中的代码(10)
  
* 使用结构数据类型：**列表、字典**等描述循环中的状态点，设备和循环性能指标(4)

* 基于数据结构的设计，使用**函数**封装计算模块，组织循环计算(3)

* 参考 [Solution of Example 8.6](./rankine86-SP.txt) 的输出，在Jupyter Notebook中输出工整的循环参数和性能指标等结果(3)

### Jupyter Notebook中的文档(5)   
    
 **格式(1)**
 
原则上采用Markdown，如果需特殊效果，可少量使用HTML/CSS; 公式用LaTex(MathJax)

**内容**

* 问题描述(1)
        
* 设计思路(1)
        
* 模块说明(1)
       
* 小结(1) 

## Tips

You may use [Jupyter Notebook of Example 8.6](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle86-Step0.ipynb) to start the practice

**Results for reference**

* [Solution of Example 8.6](./rankine86-SP.txt)

**Jupyter notebooks for reference**
       
* [Jupyter notebooks of Example 8.1 @PySEE/PyRankine](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle81-82-Step0-1.ipynb)

* [Jupyter Notebook of Example 8.6](https://nbviewer.ipython.org/github/PySEE/PyRankine/blob/master/notebook/RankineCycle86-Step0.ipynb)

**Download the ebook**

Michael J . Moran. Fundamentals of Engineering Thermodynamics(7th Edition).  John Wiley & Sons, Inc. 2011 

Download the ebook from SEU: http://www.lib.seu.edu.cn/ （查找资源->外文电子书->Wiley电子教材->T(工业技术)->TK(能源与动力工程)->TK1(热力工程,热机)）

## Directories and Files

```bash
 ├──<Practices>
 │   │ 
 │   |── <P2>
 │   │    │ 
 │   │    |── start.bat (内容为jupyter notebook的bat文件)
 │   │    │ 
 │   │    |── *.ipynb  (Example 8.6循环分析ipynb文件)
 │   │    |
 │   │    |── <img> 存放ipynb文件中使用的图片文件
                 |
                 │ ── *.jpg/png
``` 

## 提交：

* 1 电邮： cmh@seu.edu.cn
   
  * 主题：学号-姓名-2
  * 附件：压缩工作目录(如：P2)，命名为： **学号-姓名-2.zip**

* 2 **截至时间：** 2019.04.21
  
  * 截至时间后补交，补交得分<10. (2019.06.16)

* 3 改进更新：提交作业后可改进，改进截至时间：2019.06.16

## Reference：

* [Markdown](https://github.com/PySEE/home/blob/S2019/guide/Introduction2Markdown(Chinese).md)

* Jupyter Documentation. http://jupyter.readthedocs.org/en/latest/
    
    * IPython https://ipython.org/
    
    * A gallery of interesting notebook：https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

* [MathJax LaTeX](https://nbviewer.jupyter.org/github/PySEE/home/blob/S2019/notebook/Unit2-3-PyThermo-MathJax-LaTeX.ipynb)

* [IAPWS-IF97 high-speed shared library:SEUIF97](https://github.com/PySEE/SEUIF97)




  

