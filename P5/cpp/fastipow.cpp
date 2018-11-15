/*
g++ -o ../bin/fastipow fastipow.cpp
*/
#include <iostream>

using namespace std;

double ipow(double x, unsigned int n)
/* The Repeated Squaring Method : calculate x to the n power,
    n>=0
    returns 0.0^0 = 1.0, so continuous in x
*/
{
    double value = 1.0;
    do
    {
        if (n & 1)
            value *= x; /* for n odd */
        n >>= 1;
        x *= x;
    } while (n);

    return value;
}

int main()
{
    cout << "\nThe simple example of the repeated squaring method by" << endl;
    cout << "          Name: "<< "Change the text to your name" << endl;
    cout << "    Student ID: "<< "Change the text to your student ID" << endl;
   
    double x = 2.0;
    int n=8;  
    cout << "\n ipow(x, n): "<< x<<"^"<<n<<"="<< ipow(x, n) <<endl;
};