#!/usr/bin/python

def bubble(array):
 # This sort iterates through every item in the array, swapping elements
 # that are out of order. The largest element moves to the end of the array
 # with each iteration of the for loop
 length = len(array)
 swapped = True
 while(swapped):
  swapped = False
  for i in range(1, length):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True

def bubble_optimized1(array):
 # This sort iterates through every item in the array, swapping elements
 # that are out of order. The largest element moves to the end of the array
 # with each iteration of the for loop. Each time a loop iteration completes,
 # the last element of the previous iteration can be skipped since the last 
 # element is guaranteed to be the largest element of the previous iteration.
 length = len(array)
 swapped = True
 while(swapped):
  swapped = False
  for i in range(1, length):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    swapped = True
  length -= 1

def bubble_optimized2(array):
 # This sort is similar to bubble_optimized1, but skips more elements at the 
 # end of the array that are already sorted. The position of the last swap is 
 # recorded so that the next iteration through the array ends at the last recorded
 # swap location. Elements that are not swapped do not need to be reaccessed.
 final = len(array)
 while(final > 0):
  last = 0
  for i in range(1, final):
   if array[i - 1] > array[i]:
    array[i - 1], array[i] = array[i], array[i - 1]
    last = i
  final = last

if __name__ == '__main__':
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 bubble(numbers)
 print(numbers)
 
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 bubble_optimized1(numbers)
 print(numbers)
 
 numbers = [6, 5, 3, 1, 8, 7, 2, 4]
 print(numbers)
 bubble_optimized2(numbers)
 print(numbers)