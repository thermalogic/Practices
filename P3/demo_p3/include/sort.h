#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <stdlib.h>

void insertionSort(int a[], int size);
void selectionSort(int a[], int size);
void mergeSort(int a[], int size);
void bubbleSort(int a[], int size);
void quickSort(int a[], int size);

void print(const int a[], int iMin, int iMax);

#endif