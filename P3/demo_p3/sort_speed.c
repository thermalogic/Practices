
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>
#include <sys/time.h>
#include "sort.h"

int sort_time(void (*f)(int *a, int SIZE), int *a, int SIZE)
{
    int elapsed; //  time duration(microseconds) of sorting algorithms
    struct timeval st, et;
    gettimeofday(&st, NULL);
    f(a, SIZE);
    gettimeofday(&et, NULL);
    elapsed = ((et.tv_sec - st.tv_sec) * 1000000) + (et.tv_usec - st.tv_usec);
    return elapsed;
}

int main(int argc, char **argv)
{
    int SIZE = atoi(argv[1]); // the begin size of array
    int STEP = atoi(argv[2]); // the step size of array
    int NUM = atoi(argv[3]);  // the numbers of test

    // time duration(microseconds) of sorting algorithms
    int time_selection, time_merge;

    printf("A_size,Selection\n");
    // printf("A_size,Selection,Merge\n");

    // Performs timing
    for (int it = 0; it < NUM; it++)
    {
        int *v, *a;
        v = (int *)malloc(sizeof(int) * SIZE);
        a = (int *)malloc(sizeof(int) * SIZE);

        srand((unsigned)time(NULL));
        for (int i = 0; i < SIZE; i++)
        {
            v[i] = (int)rand() % SIZE + i;
        };

        // selection sort
        memcpy(a, v, sizeof(int) * SIZE);
        time_selection = sort_time(selection_sort, a, SIZE);

        
        // merge sort
        
        
        printf("%i, %i\n", SIZE, time_selection);
        
        free(v);
        free(a);

        SIZE += STEP; // increases the size of array by STEP
    }

    return 0;
}