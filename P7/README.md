
[![Gitter](https://badges.gitter.im/Py03013052/Students2016.svg)](https://gitter.im/Py03013052/Students2016?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## 实践作业七

以“基于IAPWS-IF97的水和水蒸汽物性计算软件包”为被测对象，

   设计基于Python标准库unittest测试类，进行物性计算正确性测试

## 推荐的工作

	  03013305   石睿     03013324  李晨光
    
    03013433 曾柯源  03013409 范永学 

## 测试内容

1.	IAPWS-IF97公式物性计算的正确性；

2.	IAPWS-IF97补充公式物性计算的正确性。

## 测试方法

   须含Test suites
## 提交内容

测试源码，测试分析报告（含测试数据和结果）。

## 提交方式

1. 文件压缩包：`学号_姓名_作业七.zip`；

2. 电邮：cmh@seu.edu.cn, 邮件主题：`学号_姓名_作业七`；

3. 推送到GitHub仓库。

## 参考代码

```python
import unittest
import seuif97

class Region1Test (unittest.TestCase):

    def setUp(self):
         self.T0=273.15

         # IF97-dev,Table 5 Page 9 : p,t(K),h,s
         self.tab5=[ [ 3, 300, 0.115331273e3, 0.392294792 ],
                     [80, 300, 0.184142828e3, 0.368563852 ],
                     [ 3, 500, 0.975542239e3, 0.258041912e1]]

    def testSpecificEnthalpyPT(self):
         places = 6
         for item in  self.tab5:
             self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,4),item[2],places)

    def testSpecificEntropyPT(self):
         places = 8
         for item in  self.tab5:
             self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,5),item[3],places)

if __name__ == '__main__':
    unittest.main()            
```

## 参考文献

1. IAPWS Releases, Supplementary Releases, Guidelines, and Advisory Notes
     http://www.iapws.org/release.html

2. 拷贝U盘内容中IF97目录下有下载好的IAPWS文档：

    * IAPWS-IF97公式：

      * IF97-Rev.pdf

    * 补充公式：

      * Supp-phs3-2014.pdf

      * Supp-PHS12-2014.pdf

      * Supp-Tv(ph,ps)3-2014.pdf

      * Supp-VPT3-2014.pdf

