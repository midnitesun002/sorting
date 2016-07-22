#!/usr/bin/python

# Reference: https://en.wikipedia.org/wiki/Cocktail_sort

def cocktail(array):
 # This sort iterates through every item in the array, swapping elements
 # that are out of order. It starts by traversing the list forward; once the
 # end is reached, this function traverses the list backwards until reaching
 # the beginning, and repeats the process until no more elements are swapped.
 final = len(array)
 start = 1
 swapped = True
 while(swapped):
  swapped = False
  for i in range(start, final):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True
  for i in range(final - 1, start - 1, -1):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True

def cocktail_optimized1(array):
 # This is just like cocktail sort, except the start and final search indexes
 # are reduced by one with each iteration of the sort. The largest/smallest
 # element should be inserted at each end of the array with each iteration,
 # so there is no need to acces each end of the array after one loop completes.
 final = len(array)
 start = 1
 swapped = True
 while(swapped):
  swapped = False
  for i in range(start, final):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True
  final -= 1
  for i in range(final - 1, start - 1, -1):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True
  start += 1

def cocktail_optimized2(array):
 final = len(array)
 start = 1
 while(start < final):
  last = start
  for i in range(start, final):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    last = i
  final = last
  first = final
  for i in range(final - 1, start - 1, -1):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    first = i
  start = first
  
if __name__ == '__main__':
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 cocktail(numbers)
 print(numbers)
 
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 cocktail_optimized1(numbers)
 print(numbers)
 
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 cocktail_optimized2(numbers)
 print(numbers)