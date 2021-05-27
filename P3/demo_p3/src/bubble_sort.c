#include "sort.h"

// A function to implement bubble sort
void bubble_sort(int a[], int size)
{
    bool done = false; // terminate if no more swap thru a pass
    int temp;          // use for swapping

    for (int i = 1; i < size; i++)
    {
        done = true;
        // Last i elements are already in place
        for (int j = 0; j < size - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                done = false;  // swap detected, one more pass
            }
        }
        if (done)
            break;
    }
}