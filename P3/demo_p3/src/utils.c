
#include "sort.h"

// Print the contents of the array in [iMin, iMax]

void print(const int a[], int iMin, int iMax)
{
    printf("{");
    for (int i = iMin; i <= iMax; ++i)
    {
        printf("%d", a[i]);
        if (i < iMax)
            printf(",");
    }
    printf("}");
}
