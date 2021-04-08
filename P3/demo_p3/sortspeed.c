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
  int COUNTS = 100;
  for (int i = 0; i < COUNTS; i++)
  {
    f(a, SIZE);
  }
  clicks = (clock() - start);
  double sec = (double)clicks / CLOCKS_PER_SEC;
  print(a, 0, 10);
  printf("\n");
  printf("The %s take %ju clicks(%.6f second) on %d times", sortname, (uintmax_t)(clock_t)clicks, sec, COUNTS);
}

int main()
{
  const int SIZE = 100000;
  int *a;
  a = (int *)malloc(sizeof(int) * SIZE);

  srand((unsigned)time(NULL));
  for (int i = 0; i < SIZE; i++)
  {
    a[i] = (int)rand() % (SIZE * 5) + 1;
  };
  print(a, 0, 10);
  printf("\n");

  sortingtimes(bubbleSort, "bubbleSort", a, SIZE);

  free(a);
  return EXIT_SUCCESS;
}
