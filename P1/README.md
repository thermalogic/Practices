## Practice 1(15)

**Basic Programming**: Python,Jupyter,Visual Studio Code，MinGW-W64,Github

Deadline: 

## 练习内容

了解课程教学内容；参考 [The Guide of Building Software Environment](https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md), 建立软件开发环境; 编写简单代码，练习软件操作，完成相应的Word文档。

**1** 了解Github给出简介

**2** 建立Github账户，Fork不少于2个和课程学习内容有关的Github仓库到个人Github账户；
  
**3** 安装Python解释器和软件包autopep8, pylint；用IDLE编一个简单Python程序： 代码中须有输出本人的学号和姓名的print语句。(不是使用 **Python Shell**解释输入的Python语句，是使用 **File** 编辑和运行Python程序源码)
  
         科学计算等软件包可本次练习后，根据学习进度逐步安装`  

**4** 安装Jupyter, 编写一个Jupyter Notebook交互计算文件(ipynb)
  
 从 [INTRODUCTION_TO_PYTHON](http://nbviewer.jupyter.org/github/PySEE/home/blob/S2019/notebook/Unit1-1-02-INTRODUCTION_TO_PYTHON.ipynb)中任选一小段文本和代码，编写练习要求的Jupyter Notebook文件： 
   
  * 1）文本部分加上自己的学号和姓名（Markdown格式）
  * 2）代码部分加上用print输出自己的学号和姓名（Python3）

**5** 安装MinGW-W64，Visual Studio Code和Python，C/C++插件； 用VS Code编写Python、C/C++程序
   
* Python程序：从[INTRODUCTION_TO_PYTHON](http://nbviewer.jupyter.org/github/PySEE/home/blob/S2019/notebook/Unit1-1-02-INTRODUCTION_TO_PYTHON.ipynb)中任选一段代码，代码加上用print输出自己的学号和姓名。

* C++程序: 使用VS Code修改 [hello.cpp](./cpp/hello.cpp) 代码， 将其中的"Change the text to your name"和"Change the text to your student ID"，修改为自己的姓名( **用拼音，不要用中文** ）和学号，使用MinGW-W64编译、运行. 

```cpp 
#include <iostream>
using namespace std;
 
int main() {
   cout << "      Name: "<<"Change the text to your name(PIN YIN)"<<endl;
   cout << "Student ID: "<<"Change the text to your student ID"<<endl;
   return 0;
}
```

**6** 编写软件环境建立、程序设计过程和工作小结的文档。文档使用微软Word2007以上版本docx格式。

## Word文档内容

  * 1 Github简介(1)
   
  * 2 本人Github账户名，使用的电邮；账户主页面截图(fork仓库后)(1)
 
## 练习目录和文件组织

```bash
 ├──<Practices>
 │   │ 
 │   |── <P1>
 │   │    │ 
 │   │    |── 学号-姓名-1.docx
 │   │    │ 
 │   │    |── <python>: 存放练习中python源码文件夹, 文件名不要使用中文
 │   │    |           |
 │   │    |           │ ── *.py
 │   │    |
 │   │    |── <cpp>:  存放练习中C/C++源码文件夹, 文件名不要使用中文
 │   │    |           |
 │   │    |           │ ── *.c/cpp
 │   │    │ 
 │   │    │── <notebook> 存放练习中Jupyter Notebook等文件夹, 文件名不要使用中文
 │   │                  │
 │   │                  │── start.bat: 内容为jupyter notebook的bat文件 
 │   │                  │     
 │   │                  |── *.ipynb
 │   │
 |   │ ── <P2>
 │   │ 
```

## 电邮提交：

将练习目录(如：P1)压缩为：**学号-姓名-1.zip**

* 1 电邮：cmh@seu.edu.cn

  * 主题：学号-姓名-1
  
  * 附件：学号-姓名-1.zip

* 2 **截至时间：** 

  * 截至时间后可补交，补交得分<=3.

## 参考：

* [The Guide of Building Software Environment](https://github.com/PySEE/home/tree/S2019/guide/BuildingSoftwareEnvironment.md) 

  * [Computer Terminal](https://github.com/PySEE/home/tree/S2019/guide/ComputerTerminal.md)

  * [Windows File System](https://github.com/PySEE/home/tree/S2019/guide/WindowsFileSystem.md) 

* [Problem and Answer](https://github.com/PySEE/home/tree/S2019/guide/Problem_Solution.md) 

* 知乎：怎样使用GitHub. http://www.zhihu.com/question/20070065
 
