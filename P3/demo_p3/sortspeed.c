#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include "sort.h"

void sortingtimes(void (*f)(int a[], int SIZE), char *sortname, int a[], int SIZE);

void sortingtimes(void (*f)(int a[], int SIZE), char *sortname, int a[], int SIZE)
{
  clock_t start = clock();
  clock_t clicks;
  
  f(a, SIZE);
  
  clicks = (clock() - start);
  double sec = (double)clicks / CLOCKS_PER_SEC;
  print(a, 0, 20);
  printf("\n");
  printf("The %s take %ju clicks(%.6f second) on %d size", sortname, (uintmax_t)(clock_t)clicks, sec, SIZE);
}

int main()
{
  const int SIZE = 10000;
  int *a;
  a = (int *)malloc(sizeof(int) * SIZE);

  srand((unsigned)time(NULL));
  for (int i = 0; i < SIZE; i++)
  {
    a[i] = (int)rand() % (SIZE *10) + 1;
  };
  print(a, 0, 20);
  printf("\n");

  sortingtimes(bubbleSort, "bubbleSort", a, SIZE);

  free(a);
  return EXIT_SUCCESS;
}
