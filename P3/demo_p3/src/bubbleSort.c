/* Sorting an array using Bubble Sort (BubbleSort.c) */

#include "sort.h"

// Sort the given array of size
void bubbleSort(int a[], int size)
{
   int done = 0; // terminate if no more swap thru a pass
   int temp;     // use for swapping

   while (done == 0)
   {
      done = 1;
      // Pass thru the list, compare adjacent items and swap
      // them if they are in wrong order
      for (int i = 0; i < size - 1; ++i)
      {
         if (a[i] > a[i + 1])
         {
            temp = a[i];
            a[i] = a[i + 1];
            a[i + 1] = temp;
            done = 0; // swap detected, one more pass
         }
      }
   }
}
