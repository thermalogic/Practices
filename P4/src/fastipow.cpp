/*
g++ -o ../bin/fastipow fastipow.cpp
../bin/fastipow
*/
#include <iostream>

using namespace std;

double ipow(double x, int n);

int main()
{
    cout << "\nThe simple example of the repeated squaring method by" << endl;
    cout << "          Name: "
         << "Change the text to your name" << endl;
    cout << "    Student ID: "
         << "Change the text to your student ID" << endl;

    double x = 2.0;
    int n = 8;
    cout << "\n ipow(x, n): " << x << "^" << n << "=" << ipow(x, n) << endl;
};

/*  
    ipow:  repeated squaring method
        https://en.wikipedia.org/wiki/Exponentiation_by_squaring
*/
double ipow(double x, int n)
{
    double value = 1.0;

    if (!n)
        return 1.0; /* x^0 = 1 */

    if (n == 1)
        return x;

    if (x == 0.0)
        return 0.0; /* 0^n = 0 */

    if (n < 0)
    {
        n = -n;
        x = 1.0 / x;
    }

    do
    {
        if (n & 1) /* n is odd */
            value *= x;
        n >>= 1; /* n/2  */
        x *= x;
    } while (n);

    return value;
}