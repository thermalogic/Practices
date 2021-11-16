
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>

#include "sort.h"

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
    int STEP = 10000;   //the step size of array
    const int NUM = 10; // the numbers of test sample

    // Arrays to store time duration of sorting algorithms
    int time_selection[NUM], time_merge[NUM];

    printf("A_size,Selection\n");
    // printf("A_size,Selection,Merge\n");

    // Performs number iterations
    for (int it = 0; it < NUM; it++)
    {
        // increases the size of array by STEP
        SIZE += STEP;

        int *v;
        int *a;
        v = (int *)malloc(sizeof(int) * SIZE);
        a = (int *)malloc(sizeof(int) * SIZE);

        srand((unsigned)time(NULL));
        for (int i = 0; i < SIZE; i++)
        {
            v[i] = (int)rand() % SIZE + i;
        };

        // selection sort
        memcpy(a, v, sizeof(int) * SIZE);
        time_selection[it] = sortingtimes(selection_sort, a, SIZE);

        //  merge sort
        //

        printf("%i, %i\n", SIZE, time_selection[it]);
        //
        
        free(v);
        free(a);
    }

    return 0;
}