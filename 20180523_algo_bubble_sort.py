# https://www.geeksforgeeks.org/bubble-sort/

"""
In-place bubblesort
"""


def bubble_sort(in_list):
  n = len(in_list)
  for i in range(n):
    for j in range(0, n-i-1):
      if in_list[j] > in_list[j+1]:
        in_list[j], in_list[j+1] = in_list[j+1], in_list[j]

  return in_list




import random
print(bubble_sort([random.randint(0,10) for i in range(10)]))