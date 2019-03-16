/*
Compiling:
 
   g++ -o hello hello.cpp

Compiling for output Chinese to console in GBK

   g++ -o hello hello.cpp -fexec-charset=GBK

Running

  For PowerShell 

     ./hello

  For cmd

     hello

*/
#include <iostream>
using namespace std;
 
int main() {
   cout << "      Name: "<<"Change the text to your name(PIN YIN)"<<endl;
   cout << "Student ID: "<<"Change the text to your student ID"<<endl;
   return 0;
}
