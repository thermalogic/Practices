
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>

#include "sort.h"

int sortingtimes(void (*f)(int *a, int SIZE), int *a, int SIZE);

int sortingtimes(void (*f)(int *a, int SIZE), int *a, int SIZE)
{
    clock_t start = clock();
    f(a, SIZE);
    double clicks = (double)(clock() - start);
    return (int)clicks;
}

int main()
{
    int SIZE = 0;       //the begin size of array
    int STEP = 1000;    //the step size of array
    const int NUM = 10; // the numbers of test sample

    // Arrays to store time duration of sorting algorithms
    int time_bubble[NUM], time_merge[NUM], time_insertion[NUM], time_quick[NUM];

    printf("A_size,Bubble\n");

    // printf("A_size,Bubble,Merge,Insertion,Quick\n");

    // Performs number iterations
    for (int it = 0; it < NUM; it++)
    {
        // increases the size of array by 10000
        SIZE += STEP;

        int a[SIZE], v[SIZE];
        srand((unsigned)time(NULL));
        for (int i = 0; i < SIZE; i++)
        {
            v[i] = (int)rand() % (SIZE * 5) + 1;
        };

        // Bubble sort
        memcpy(a, v, sizeof(int) * SIZE);
        time_bubble[it] = sortingtimes(bubbleSort, a, SIZE);

        // add code for Merge,Insertion,Quick Sort
        // merge sort
        //memcpy(a, v, sizeof(int) * SIZE);
        //time_merge[it] = sortingtimes(mergeSort, a, SIZE);

        printf("%i, %i\n",
               SIZE,
               time_bubble[it]);

        /*printf("%i, %i, %i, %i, %i\n",
               SIZE,
               time_bubble[it],
               time_merge[it],
               time_insertion[it],
               time_quick[it]      
               );
        */
    }

    return 0;
}