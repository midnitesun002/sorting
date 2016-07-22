#!/usr/bin/python

# Reference: https://en.wikipedia.org/wiki/Merge_sort

import timeit

def merge_naive(array):
 # recursive, small dataset, array
 N = len(array)
 if N > 1:
  left = merge_naive(array[:int(N/2)])
  right = merge_naive(array[int(N/2):])
  lN, rN = len(left), len(right)
  i, j, k = 0, 0, 0
  array = [0 for k in range(lN + rN)]
  while(i < lN and j < rN):
   if left[i] < right[j]:
    array[k] = left[i]
    i += 1
   else:
    array[k] = right[j]
    j += 1
   k += 1
  if i < j:
   array[k:] = left[i:]
  else:
   array[k:] = right[j:]
 return array

def merge(array, iBegin, iEnd, work):
 if(iEnd - iBegin < 2):
  return
 iMiddle = int((iEnd + iBegin) / 2)
 merge(array, iBegin, iMiddle, work)
 merge(array, iMiddle, iEnd, work)
 combineInWork(array, iBegin, iMiddle, iEnd, work)
 array[iBegin:iEnd] = work[iBegin:iEnd]

def combineInWork(array, iBegin, iMiddle, iEnd, work):
 i, j = iBegin, iMiddle
 for k in range(iBegin, iEnd):
  if(i < iMiddle and (j >= iEnd or array[i] <= array[j])):
   work[k] = array[i]
   i += 1
  else:
   work[k] = array[j]
   j += 1

if __name__ == '__main__':
 #numbers = [6, 5, 3, 1, 9, 8, 7, 2, 4]
 #print(numbers)
 #numbers = merge(numbers)
 #print(numbers)
 setup = 'from __main__ import merge_naive; numbers = [6, 5, 3, 1, 9, 8, 7, 2, 4]'
 t = timeit.Timer('ans = merge_naive(numbers)', setup)
 print(t.timeit(10000))
 print(t.repeat(3,1000))
 setup = """
from __main__ import merge, combineInWork
numbers = [6, 5, 3, 1, 9, 8, 7, 2, 4]
work = [0 for i in range(len(numbers))]
 """
 t = timeit.Timer('ans = merge(numbers, 0, len(numbers), work)', setup)
 print(t.timeit(10000))
 print(t.repeat(3,1000))
 
 numbers = [6, 5, 3, 1, 9, 8, 7, 2, 4]
 work = [0 for i in range(len(numbers))]
 print(numbers)
 merge(numbers, 0, len(numbers), work)
 print(numbers)