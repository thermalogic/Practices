/*
 Sorting an array using Selection Sort 
*/

#include "sort.h"

// Sort the given array of size using selection sort
void selection_sort(int a[], int size)
{
    int temp; // for swaping
    for (int i = 0; i < size - 1; ++i)
    {
        // [0, i-1] already sort
        // Search for the smallest element in remaining unsorted array [i, size-1] and swap with a[i]
        int min_idx = i; // assume fist element is the smallest in remaining unsorted array [i, size-1]
        for (int j = i + 1; j < size; ++j)
        {
            if (a[j] < a[min_idx])
                min_idx = j;
        }
        if (min_idx != i)
        { // swap
            temp = a[i];
            a[i] = a[min_idx];
            a[min_idx] = temp;
        }
    }
}
