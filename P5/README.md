
## Practice 4

**Unit Test**(5)：IAPWS-IF97 physical properties calculation and unit test  

Deadline: 2018.06.05

## 要求(5分)：

* 根据：
     
     Revised Supplementary Release on Backward Equations for Specific Volume
      as a Function of Pressure and Temperature v(p,T)
     for Region 3 of the IAPWS Industrial Formulation 1997 for the 
     Thermodynamic Properties of Water and Steam

     http://www.iapws.org/relguide/Supp-VPT3-2016.pdf

 中提供的v(p,T)计算公式，设计物性计算及单元测试程序：

 * 1 物性计算(2)：Supp-VPT3-2016.pdf中划分的Region 3子区域（3a~3z)，

    * 按照学号 01->3a, .., 26->3z, 27->3a, 28->3b, ....  选择子区域，实现Supp-VPT3-2016.pdf中补充公式的v(p,T)计算

       如：03015301，03015401 做3a子区域

 * 2 单元测试(3)：基于unittest的物性计算程序的测试单元
 
## 提交：

* 1 电邮：cmh@seu.edu.cn 
    
  * 主题：学号-姓名-5
    
  * 附件：程序文件压缩包：**学号-姓名-5.zip**

* 2 截至时间：2018.06.05

  * 截至时间后可补交，最分<=7. (2018.06.15)

* 3 改进更新：提交作业后可改进，改进截至时间：2018.06.15

## IAPWS Releases： 

IAPWS Releases, Supplementary Releases, Guidelines, and Advisory Notes:

http://www.iapws.org/release.html
              
* 1 Releases：IAPWS-IF97
           
  * IF97-Rev http://www.iapws.org/relguide/IF97-Rev.html
            
  * IF97-Rev.pdf  http://www.iapws.org/relguide/IF97-Rev.pdf

 * 2 Supplementary Releases：
      
   * SR2-01 http://www.iapws.org/relguide/Supp-PHS12-2014.pdf
        
   * SR3-03 http://www.iapws.org/relguide/Supp-Tv(ph,ps)3-2014.pdf
        
   * SR3-04 http://www.iapws.org/relguide/Supp-phs3-2014.pdf
        
   * SR5-05 http://www.iapws.org/relguide/Supp-VPT3-2016.pdf

## Reference：

* 2013级 https://github.com/PySEE/Practices/tree/S2016/P7

* 2014级 https://github.com/PySEE/Practices/tree/S2017/P5

* Python版的IAPWS-IF97 https://github.com/jjgomera/iapws

