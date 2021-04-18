#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>
#include "sort.h"

void sortingtimes(void (*f)(int a[], int SIZE), char *sortname, int a[], int SIZE);

void sortingtimes(void (*f)(int a[], int SIZE), char *sortname, int a[], int SIZE)
{
  clock_t start = clock();

  f(a, SIZE);

  double sec = (clock() - start) / (double)CLOCKS_PER_SEC;
  printf("\n");
  print(a, 0, 20);
  printf("\n");
  printf("The %s take %.6f second on %d size", sortname, sec, SIZE);
}

int main()
{
  const int SIZE = 10000;
  int *b;
  b = (int *)malloc(sizeof(int) * SIZE);

  srand((unsigned)time(NULL));
  for (int i = 0; i < SIZE; i++)
  {
    b[i] = (int)rand() % (SIZE * 10) + 1;
  };
  print(b, 0, 20);
  printf("\n");

  int *a;
  a = (int *)malloc(sizeof(int) * SIZE);

  memcpy(a,b, sizeof(int) * SIZE);
  sortingtimes(bubbleSort, "bubbleSort", a, SIZE);

  //memcpy(a,b sizeof(int) * SIZE);
  //sortingtimes(mergeSort, "mergeSort", a, SIZE);

  free(b);
  free(a);
  return EXIT_SUCCESS;
}
