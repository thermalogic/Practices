## Practice 2

**Python and Interactive Computing**(15)：The Simple Simulator of Rankine Cycle 
  
* Purpose：**Jupyter Notebook**: shareing the code and reproducible research

* Deadline: 2018.04.24
  
## The Rankine Cycle: 

Michael J. Mora. Fundamentals of Engineering Thermodynamics (7th Edition).  John Wiley & Sons, Inc. 2011

(Please search web to download the PDF,e.g http://muchong.com/html/201501/8475071.html  or  http://ishare.iask.sina.com.cn/f/34258437.html )

Chapter 8 Vapor Power System:(Page 460-463)

* Example 8.6 : Considering a Reheat–Regenerative Cycle with Two Feedwater Heaters, a closed feedwater heater and an open feedwater heater. 

  * [Example 8.6](./rankine86.md) 

  * [Solution of Example 8.6](./rankine86-SP.txt)

## 要求：(总分15)

### 1 文件类型：Jupyter Notebook(Python 3)
    
### 2 Jupyter Notebook程序:
    
*  **代码部分**(10)：
  
   * 使用结构数据类型：**元组、列表、字典**等

   * 使用**函数**封装方法；
   
   >**要点提示：**
       
     * 1 用怎样的数据结构描述循环中：
        
        * 状态点？

        * 设备？

        * 循环性能指标等参数？

    * 2 计算的基本步骤组成、对应的函数安排、在1的基础上实现函数

    * 3 在1、2的基础上，给定计算条件，计算循环。  

    * **参考设计:**
       
       * PyRankine https://github.com/PySEE/PyRankine  step0, step1

       * Excel4Engineering https://github.com/PySEE/Excel4Engineering  Rankine81-0.xlsm,Rankine81-1.xlsm   
     
* **文档部分**(5);   
    
    * 格式：使用Markdown，公式用Mathjax; 中英文皆可。

    * 内容：

      * 问题描述
        
      * 设计思路
        
      * 模块说明
        
      * 小结 

> **注意：** 需要合理组织Notebook中文档和代码的顺序，如：先交待被计算对象，然后，设计思路，进一步是文档和相关代码，最后，小结      

## 提交：

* 1 电邮： cmh@seu.edu.cn
   
  * 主题：学号-姓名-2
  * 附件：Jupyter Notebook等文件的压缩包： **学号-姓名-2.zip**；

* 2 **截至时间：** 2018.04.24
  
  * 截至时间后补交，补交得分<10. (2018.06.15)

* 3 改进更新：提交作业后可改进，改进截至时间：2018.06.15

## 参考资源：

*  Jupyter Notebook of IdealRankineCycle http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/PyThermo_IdealRankineCycle.ipynb
 
*  PyRankine https://github.com/PySEE/PyRankine

*  Excel4Engineering https://github.com/PySEE/Excel4Engineering  

*  Jupyter Notebook for Fundamentals of Engineering Thermodynamics, Michael J . Mora. 

   * https://github.com/FOSSEE/Python-Textbook-Companions/tree/master/Fundamental_of_Thermodynamics_by_Moran_and_Shapiro_by_Michael_J._Moran_and_Howard_N._Shapiro
   
     * Chapter_8.ipynb

* Jupyter Documentation. http://jupyter.readthedocs.org/en/latest/
    
    * IPython https://ipython.org/
    
    * A gallery of interesting notebook：https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks



  

