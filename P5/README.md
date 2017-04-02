
## 课程实践五：

* **单元测试** (10)：IAPWS-IF97水和水蒸汽物性计算及单元测试 

## 推荐的工作 

-----
| 序号  |1          |    2 |
| ------|:--------:| -----------:|
| 学号  | 030143**  |  030144**   |
| 姓名  |           |             |
---------


## 要求（10分）：

* 根据：
     Revised Supplementary Release on Backward Equations for Specific Volume
      as a Function of Pressure and Temperature v(p,T)
     for Region 3 of the IAPWS Industrial Formulation 1997 for the 
     Thermodynamic Properties of Water and Steam

* 中提供的v(p,T)计算公式，设计物性计算及单元测试程：

 * 1）物性计算(3)：Supp-VPT3-2016.pdf中划分的Region 3子区域（3a~3z)，

        按照学号 01-3a, .., 26-3z, 27-3a, 28-3b, ....  选择子区域，实现其v(p,T)计算
        如：03014301，03014401 做3a子区域

 * 2）单元测试(3)：基于unittest的物性计算程序的测试单元
 * 3）代码质量(4)：数据结构、模块组织，PEP8

## 提交：

* 1） 电邮：cmh@seu.edu.cn 
    
      主题：学号-姓名-P5
    
      附件：程序文件压缩包：**学号-姓名-P5.zip**

* 2）	 截至时间：2017.05.28

        过截至时间后可以补交，补交作业最高6分

* 3）	改进更新：提交作业后可改进，改进截至时间：2017.06.04

## 参考文献： 

* IAPWS Releases, Supplementary Releases, Guidelines, and Advisory Notes
   * http://www.iapws.org/release.html
              
     *  1）IAPWS-IF97公式：IF97-Rev.pdf
     * 2）补充公式：
                       Supp-phs3-2014.pdf
                       Supp-PHS12-2014.pdf
                       Supp-Tv(ph,ps)3-2014.pdf
                       Supp-VPT3-2016.pdf

## 参考资源：

* https://github.com/PySEE/RecommendedPractices/tree/S2016/P7

* https://github.com/jjgomera/iapws

