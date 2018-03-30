## Homeworks

* [Homework1](#homework1) : Practice 1(03.13): Github(5),etc

* [Homework2](#homework2) : Practice 2(04.24): Python and Interactive Computing(15),etc

### Homework1

* **Practice 1: Github**(5)

  * [Github、Git](https://github.com/PySEE/Practices/tree/S2018/P1)

    **Deadline:** 2018.03.13

* **Required Materials and Textbooks**
 
  * Lectures in Jupyter Notebook

    from https://github.com/PySEE/home  **download zip file** ,then unz
    
    **Note：**  After you have installed Git, you may **Clone**  
    ```bash
    >git clone https://github.com/PySEE/home.git 
    ```

  * John V. Guttag. Introduction to Computation and Programming Using Python. Revised and expanded edition. MIT Press. 2013.08.

    * Search web to **download the PDF file** of the BOOK

    * https://mitpress.mit.edu/index.php?q=books/introduction-computation-and-programming-using-python-0

    * 梁杰译. 编程导论. 人民邮电出版社(第1版) .  2015.03

     * Accompanying Python3 Code：https://mitpress.mit.edu/sites/all/modules/patched/pubdlcnt/pubdlcnt.php?file=/sites/default/files/code-978-0-262-52962-4_0.zip&nid=321887 

* **Building Software Environment**

   https://github.com/PySEE/home/tree/S2018/guide/BuildingSoftwareEnvironment.md 

  * 1 Python 
    
    * install Python
       
      https://www.python.org/ 
      
      download Python https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe then install
      
    * try using Python shell and IDLE   

  * 2 Coding Tool: Microsoft Visual Code

    * install VS code https://code.visualstudio.com/

    * try Markdown doc 
      
    * add Python extensions
   
    * install autopep8,pylint

    * try programming Python

  * 3 Jupyter 
    
    * install Jupyter http://jupyter.org/
    
    ```bash     
    >pip install jupyter
    ```  
      
    * try Jupyter Notebook

    * try programming Python

    * using Jupyter Notebook of  **Home**
    
  * 4 Scipy Packages

    * Scipy(Numpy,scipy,matplotlib)  https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
    
    ```bash
      pip install *.whl
    ```  
   
  * 5 IAPWS-IF97 packages
    
    * SEUIF97
   
    * Python's IAPWS
    
  * 6  Git for Windows:
   
    * Install Git for Windows: https://github.com/git-for-windows/git/releases

    * Clone home, Pyrankine,SEUIF97,Practices in the https://github.com/PySEE to your computer

  * 7 C/C++(optional)

    *  install Mingw-W64(GCC for Windows)

    *  add C/C++ extensions of VS code

    * try Programming C/C++

#### Working Directory of the course

Recommended working directory: **PLEASE**: Setup your working directory on a **Non-System** disk.e.g: **D:**

```
CourseSE
 │
 ├──PySEE( git clone -init, git pull - update)
 │    │
 │    ├── Home
 │    │      
 │    ├── PyRankine
 │    │        
 │    |── SEUIF97
 │    │
 │    |── Practices
 │        
 ├──Practices
 │   │ 
 │   |── P1
 │   │ 
 │   |── P2
 │   │ 
 │   |── P3
 │   │ 
 │   |── P4
 │   │ 
 │   |── P5
 │   │ 
 │   |── Bonus
 │
 ├──Softwares
 │
 ├──Others
 │

```

###  Homework2

**Practice2**

* **Python and Interactive Computing**(15)：Jupyter Notebook of the Rankine Cycle Simulator 

* **Deadline: 2018.04.24**
 
**Jupyter Notebooks**

* [01 PREFACE](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/01_PREFACE.ipynb)

* [02 INTRODUCTION TO PYTHON](http://nbviewer.ipython.org/github/PySEE/home/tree/S2017/notebook/02_INTRODUCTION_TO_PYTHON.ipynb)

* [03 SOME SIMPLE NUMERICAL PROGRAMS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/03_SOME_SIMPLE_NUMERICAL_PROGRAMS.ipynb)

* [04 FUNCTIONS SCOPING AND ABSTRACTION](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/04_FUNCTIONS_SCOPING_AND_ABSTRACTION.ipynb)

* [05 STRUCTURED TYPES MUTABILITY AND HIGHERORDER FUNCTIONS](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/05_STRUCTURED_TYPES_MUTABILITY_AND_HIGHERORDER_FUNCTIONS.ipynb)

* [PyThermo-IF97-BASIC](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/PyThermo-IF97.ipynb)

* [PyThermo-IdealRankineCycle-BASIC](http://nbviewer.ipython.org/github/PySEE/home/tree/S2017/notebook/PyThermo-IdealRankineCycle.ipynb)

* [Markdown](https://github.com/PySEE/home/blob/S2018/guide/Introduction2Markdown.md)

   * [IPYNB-MathJax-LaTeX](http://nbviewer.ipython.org/github/PySEE/home/tree/S2018/notebook/IPYNB-MathJax-LaTeX.ipynb

**Demo PyRankine**

  * step 0 :    Zero @  Data Structures,Program architecture, Algorithms(The Ideal Rankine Cycle)
                    
        simple data type and expression  only

  * step 1 :   Basic @  Data Structures,Program architecture, Algorithms(The Ideal Rankine Cycle)
                    
        list,dict,function
     
  * Jupyter Notebook

     * Step0 http://nbviewer.jupyter.org/github/PySEE/PyRankine/blob/master/notebook/IdealRankineCycle-Step0.ipynb

     * Step1 http://nbviewer.jupyter.org/github/PySEE/PyRankine/blob/master/notebook/IdealRankineCycle-Step1.ipynb