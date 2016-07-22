#!/usr/bin/python
from math import log

# Reference: https://en.wikipedia.org/wiki/Shellsort

def shell(array, gaps):
 final = len(array)
 for gap in gaps:
  for i in range(gap, final):
   temp = array[i]
   j = i
   while (j >= gap and array[j - gap] > temp):
    array[j] = array[j - gap]
    j -= gap
   array[j] = temp

 # choice of gaps affects sort time
def get_gaps(N):
 # Unknown optimal
 gaps = [701, 301, 132, 57, 23, 10, 4, 1]
 # Original gap recommendation from Shell
 gaps = [int(N/2**k) for k in range(1, int(log(N)/log(2)) + 1)]
 return gaps

if __name__ == '__main__':
 numbers = [9, 6, 5, 3, 10, 1, 8, 7, 2, 4]
 gaps = get_gaps(len(numbers))
 print(numbers)
 shell(numbers, gaps)
 print(numbers)
 print(gaps)