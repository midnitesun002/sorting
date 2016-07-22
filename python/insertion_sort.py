#!/usr/bin/python

# Reference: https://en.wikipedia.org/wiki/Insertion_sort

def insertion(array):
 unsorted = 1
 end = len(array)
 for i in range(unsorted, end):
  j = i
  while j > 0 and array[j - 1] > array[j]:
   array[j], array[j - 1] = array[j - 1], array[j]
   j -= 1
  print(i, '->', array)

if __name__ == '__main__':
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 insertion(numbers)
 print(numbers)