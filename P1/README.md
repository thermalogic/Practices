## Practice 1(15)

**Basic Programming**: Python,Jupyter,Visual Studio Code，MinGW-W64,Github and Markdown

Deadline: 2019.03.17

## 练习内容

了解课程教学内容；参考 [The Guide of Building Software Environment](https://github.com/PySEE/home/tree/S2019/guide/Beginner2BuildeSoftwareEnvironment.md),    建立软件开发环境; 编写简单代码，练习软件操作，完成相应的文档。

**1** 了解Github，PySEE中的Github仓库内容,给出简介

**2** 建立Github账户，Fork不少于2个和课程学习内容有关的Github仓库到个人Github账户，提交截图

**3** 安装Python环境,用IDLE编一个简单程序：print输出本人的学号和姓名，提交编辑源码和程序运行结果的截图

**4** 安装Jupyter, 编写一个Jupyter Notebook交互计算文件。提交交互计算文件和运行截图。
   
* 交互计算文件内容：从 **A Byte of Python：First Steps** ( https://github.com/swaroopch/byte-of-python/blob/master/first_steps.md )
   中任选2小段文字和代码，实现为jupyter notebook版本（文本：Markdown，源码：Python3).

**5** 安装MinGW-W64，Visual Studio Code和Python，C/C++插件, 编写程序，提交源码和程序编写和运行截图。
   
* Python程序：从 **A Byte of Python：First Steps** ( https://github.com/swaroopch/byte-of-python/blob/master/first_steps.md )
   中任选一段代码 

* C++程序: 使用VS Code修改 [hello.cpp](./cpp/hello.cpp) 代码， 将其中的"Change the text to your name"和"Change the text to your student ID"，修改为自己的姓名和学号，使用MinGW-W64编译运行. 提交修改后的源码，使用Visual Studio Code编辑代码和运行的截图

```cpp  
/*
g++ -o hello hello.cpp
*/
#include <iostream>
using namespace std;
 
int main() {
   cout << "Your Name: "<<"Change the text to your name"<<endl;
   cout << "Your Student ID: "<<"Change the text to your student ID"<<endl;
   return 0;
}
```

![vscode-gcc](./img/vscode-gcc.jpg)


**6** 编写软件环境建立、程序设计过程和工作小结文档。文档使用 **Markdown** 格式

## Markdown文档内容

  * 1 Github简介；PySEE中的Github仓库:Home,PyRankine,SEUIF97简介(3)
   
  * 2 本人Github账户名，使用的电邮；账户主页面截图(fork仓库后)(1)
  
  * 3 Python环境及软件包的安装过程简要说明；使用IDLE编程和运行结果的截图(2)
  
  * 4 Jupyter Notebook安装过程的简要说明；Jupyter Notebook文档的运行截图 (2)

  * 5 安装MinGW-w64,Visual Studio code和Python，C/C++插件过程的简要说明；使用VS Code编写运行简单的Python,C++程序的截图 (3)
  
  * 6 工作小结(2)

  * 7 Markdown文档格式(2)

## Markdown文档编辑提示

* 1 使用Visual Studio Code编辑Markdown文档；只使用基本的Markdown格式标志符号，不使用HTML

* 2 Markdown文档使用到的不同类型文件用相应的目录进行组织

* 3 插入图片时，需要注意图片所在目录位置：如vscode-cpp.jpg在README.md文件所在目录的下一级目录/img中，格式标志：`![vscode-cpp](./img/vscode-cpp.jpg) `

## 参考的目录和文件组织方式

**注意**： 目录和文件名都用 **`英文`**，同时注意 **`大小`** 写。Linux操作系统和Windows不同:(1) 默认的中文编码是utf-8不同于Windows的GBK; (2) 目录和文件名区分大小写。为了使我们的工作内容在不同操作系统中都能正常使用，目录和文件名都使用 **`英文`**，同时注意 **`大小`** 写。


```bash
 ├──<Practices>
 │   │ 
 │   |── <P1>
 │   │    │ 
 │   │    |── README.md :练习markdown文件
 │   │    │ 
 │   │    |── <img>: README.md文件中使用的图形文件
 │   │    │ 
 │   │    |── <python>: 练习的python源码
 │   │    |
 │   │    |── <cpp>: 练习的C++源码
 │   │    │ 
 │   │    │── <notebook> ── start.bat: 内容为jupyter notebook的bat文件 
 │   │                  │     
 │   │                  |── Jupyter Notebook文件
 │   │
 |   │ ── <P2>
 │   │ 
```

## 电邮提交：

将练习目录压缩为：**学号-姓名-1.zip** (Markdown文档（含链接的图片文件），Python程序源码，jupyter notebook文件等)

* 1 电邮：cmh@seu.edu.cn

  * 主题：学号-姓名-1
  
  * 附件： 学号-姓名-1.zip

* 2 **截至时间：** 2019.03.17

  * 截至时间后可补交，补交得分<=10. (2019.06.16)

* 3 改进更新：提交作业后可改进，改进截至时间：2019.06.16

## 参考：

* [Guide of  Building Software Environment for Beginners](https://github.com/PySEE/home/tree/S2019/guide/Beginner2BuildeSoftwareEnvironment.md) 

* [Building Software Environment](https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md)

* [Introduction to Markdown](https://github.com/PySEE/home/blob/S2019/guide/Introduction2Markdown.md)

* 03013级 
   * https://github.com/PySEE/Practices/tree/S2016/P1  

   * https://github.com/PySEE/Practices/tree/S2016/P2

* 03014级 
  * https://github.com/PySEE/Practices/tree/S2017/P1 

  * https://github.com/PySEE/Practices/tree/S2017/P2 

* 03015级 https://github.com/PySEE/Practices/tree/S2018/P1  

* Python https://www.python.org/

   * Guido van Rossum, Python development team. Python Tutorial. https://docs.python.org/3/tutorial/index.html

   * Swaroop C H. A Byte of Python：https://github.com/swaroopch/byte-of-python

* Jupyter. http://jupyter.org/
    
    * Jupyter Documentation. http://jupyter.readthedocs.org/en/latest/
    
    * IPython https://ipython.org/
    
    * A gallery of interesting notebook： https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

* Visual Studio Code: https://code.visualstudio.com/
  
   * Documentation: https://code.visualstudio.com/docs

   * **Markdown** and VS Code： https://code.visualstudio.com/docs/languages/markdown

   * Getting Started with **Python** https://code.visualstudio.com/docs/python/python-tutorial

   * **C/C++** for VS Code： https://code.visualstudio.com/docs/languages/cpp

   * **Git** Version Control in VS Code：https://code.visualstudio.com/docs/editor/versioncontrol

* GCC, the GNU Compiler Collection：http://gcc.gnu.org/

   * MinGW-W64:GCC for Windows 64 & 32 bits：http://mingw-w64.org/

   * GCC and Make：Compiling, Linking and Building C/C++ Applications http://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html

* Markdown
  
   * [CommonMark](http://commonmark.org/)
  
   * [WIKI Markdown](https://en.wikipedia.org/wiki/Markdown)

   * [Github: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
   
   * 王树义. 如何用Markdown写论文？ http://blog.sciencenet.cn/blog-377709-1088215.html

* Git,Github

   * 知乎：怎样使用GitHub. http://www.zhihu.com/question/20070065

   * The Simple Guide of Github https://github.com/PySEE/home/blob/S2019/guide/TheSimpleGuide2Github.md

   * DevTools-Git  http://nbviewer.jupyter.org/github/PySEE/home/blob/S2019/notebook/DevTools-Git.ipynb

   * How to get started with GIT and work with GIT Remote Repo http://www3.ntu.edu.sg/home/ehchua/programming/howto/Git_HowTo.html

   * git-for-windows：https://github.com/git-for-windows/git/releases
 
   * Scott Chacon，Ben Straub. Pro Git. https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

