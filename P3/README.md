## Practice Three

**Interactive Computing**(15)：Jupyter Notebook of the Rankine Cycle Simulator 
  
* Purpose： 
   * The Rankine Cycle Simulator: training computational thinking and  programming skills   
   * Jupyter Notebook: shareing the code and reproducible research

* Deadline: 2017.05.28

* **Recommended Programs**

|03014402 |  03014404 |03014316 |03014333 | 03014407 | 03014420 |  03014323 |03014304 |
|:-------:| -------:|--------:|---------:|------:|------------:|---------:|----------:|
| 吉珣碧  | 姚依晨   | 田康宁  |  马瑞     | 吴钊   |    王统伟     |陈子聿   |萨仁图娅 |


* **Students who have submitted the program**

|03014316 |03014323 |03014306 |03014333 | 03014329 |3014308 | 03014313|03014311|03014326|
|-------:|---------:|--------:|--------:|---------:|-------:|-------:|--------:|------:|
| 田康宁 | 陈子聿    |  李晗    | 马瑞    |  孔祥琛  | 陈怡睿  | 曾令超 |  骆应东  | 杨震   |

|03014328 |03014327 |03014309|03014310 |03014302 |03014304 |03014303 |03014303 |03014332 |
|--------:|--------:|--------:|--------:|-------:|--------:|-------:|-------:|------:|
| 田星宇  | 陈 克    | 叶佳威  | 余印振   | 姜牧笛  |萨仁图娅 | 徐诗越 | 李笑笑 | 梁晓迪| 


|03014402  | 03014404 |03014413 |03014407 |03014425 |03014430 |03014408 | 03014426 |03014405|
|:--------:| --------:|--------:|-------:|--------:|--------:|-------:|------:|-----:|
|  吉珣碧   | 姚依晨   |   张立奇 | 吴钊   | 付童方   | 孟华宁  |王晓艺  | 金弘琨  | 朱雪莲| 


| 03014433 | 03014420|03014406|03014423|03014424|03014419|03014429|03014427|03014411|
|---------:|---------:|-------:|-------:|-------:|-------:|-------:|------:|----:|
|   周鹏   |  王统伟  |  张贵雯 |   王越  |邢宏壮  | 罗健威  | 贺伟东   | 张翔  | 钱琪 |


| 03014410 | 03014418 | 03014401 | 
|---------:|--------:|-------:|
|  刘兵兵  |  包智明   |   沙于程   |  


用类描述系统中对象来计算，程序代码比直接计算多了不少，程序设计难度也大了很多。

为什么要这样？

因为，程序设计需要考虑一般性，给出Rankine循环通用计算分析程序设计方案是我们的目标，不是就事论事

那么
```
    y1 =
    y2 = ((1 - y1)
```
就有问题，完全和具体问题绑定了。

无论 y1还是(1 - y1)：

* 1 从节点类定义来讲，是节点的流量份额属性，
* 2 从设备类定义来看，节点的流量份额可由质量、能量平衡关系（设备特性）在相应设备中计算
* 3 设备类计算中使用到的节点流量份额，有依赖关系，如：不计算闭式加热器，没有抽汽节点流量份额，就不能计算高压缸排汽节点流量份额，有个设备计算顺序问题

所以，通用的循环分析程序需要解决3个方面问题

* 1 适当的节点定义
* 2 适当的设备类定义
* 3 1、2定义上的系统分析计算方法

这个问题难度比较大，目前只有很少同学给出解决方案，同学们先思考。

自我思考的过程，远比结果重要！


## The Rankine Cycle: 

* A Reheat–Regenerative Cycle with Two Feedwater Heaters
```
Michael J . Mora. Fundamentals of Engineering Thermodynamics (7th Edition).  John Wiley & Sons, Inc. 2011

Chapter 8 vapor Power System:  （Page 460-463）

Example 8.6 : Considering a Reheat–Regenerative Cycle with Two Feedwater Heaters, a closed feedwater heater and an
open feedwater heater. 
```
   * Steam enters the first turbine at 8.0 MPa, 480°C and expands to 0.7 MPa. 

   * The steam is reheated to 440°C before entering the second turbine, where it expands to the condenser pressure of 0.008 MPa.

   * Steam is extracted from the first turbine at 2 MPa and fed to the closed feedwater heater. 

   * Feedwater leaves the closed heater at 205°C and 8.0 MPa, and condensate exits as saturated liquid at 2 MPa. 

   * The condensate is trapped into the open feedwater heater. 

   * Steam extracted from the second turbine at 0.3 MPa is also fed into the open feedwater heater, which operates at 0.3 MPa. The stream exiting the open feedwater heater is saturated liquid at 0.3 MPa. 
 
   * The net power output of the cycle is 100 MW. 

   * There is no stray heat transfer from any component to its surroundings. 

   * If the working fluid experiences no irreversibilities as it passes through the turbines, pumps, steam generator, reheater, and condenser, 

* SOLUTION

   * **Known:** A reheat–regenerative vapor power cycle operates with steam as the working fluid. Operating pressures
and temperatures are specified, and the net power output is given.

   * **Find:** Determine the thermal efficiency and the mass flow rate entering the first turbine, in kg/h.

![fig86](fig86.jpg)  

## 要求：（总分15）

* 1）	交互计算Jupytern Notebook（7分）：
   * 问题描述、计算程序、工作小结

* 2）数据结构（5分）：面向对象、系统定义、模块组织

* 2）源码质量（3分）：Python3.*、PEP8规范；

## 提交：
* 1）电邮： cmh@seu.edu.cn
   * 主题：学号-姓名-P3
   * 附件：Jupyter Notebook程序文件压缩包： **学号-姓名-P3.zip**；

* 2）截至时间：2017.05.28
   * 过截至时间后可补交，补交作业成绩最高10分

* 3）改进更新：提交作业后可改进，改进截至时间：2017.06.04

## 参考资源：

*  http://nbviewer.ipython.org/github/PySEE/home/tree/S2017/notebook/PyThermo_IdealRankineCycle.ipynb
 
*  https://github.com/PySEE/PyRankine

*  Jupyter Notebook for Fundamentals of Engineering Thermodynamics, Michael J . Mora. 

   * https://github.com/FOSSEE/Python-Textbook-Companions/tree/master/Fundamental_of_Thermodynamics_by_Moran_and_Shapiro_by_Michael_J._Moran_and_Howard_N._Shapiro
   
     * Chapter_8.ipynb

* Jupyter Documentation. http://jupyter.readthedocs.org/en/latest/
    
    * IPython https://ipython.org/
    
    * A gallery of interesting notebook：https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

* PEP 8 - Style Guide for Python Code 

   https://www.python.org/dev/peps/pep-0008/


  

