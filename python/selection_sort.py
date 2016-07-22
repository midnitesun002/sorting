#!/usr/bin/python

# Reference: https://en.wikipedia.org/wiki/Selection_sort

def selection(array):
 unsorted = 0
 end = len(array)
 for i in range(unsorted, end):
  iMin = i
  for j in range(i + 1, end):
   if array[iMin] > array[j]:
    iMin = j
  if iMin != i:
   array[i], array[iMin] = array[iMin], array[i]
  print(i, '->', array)

if __name__ == '__main__':
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 selection(numbers)
 print(numbers)