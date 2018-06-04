  # https://www.toptal.com/algorithms/interview-questions

import functools as ft
import math

"""
Design an algorithm that finds the number of ways in which you can traverse N meters by doing jumps of 1, 2, 3, 4, or 5 meter lengths.
Assume that N can be a very large number. What is the resulting complexity?
"""

from functools import lru_cache # Memoization

jumpset = [1,2,3,4,5] # Distinct set of jump sizes



@lru_cache(maxsize = 2038)
def number_of_jumps(N):
  if N == 0:
    return 1
  smaller_dists = [N - j for j in jumpset if N - j >= 0]
  number_for_smaller = [number_of_jumps(d) for d in smaller_dists]
  return sum(number_for_smaller)


print(number_of_jumps(150))
