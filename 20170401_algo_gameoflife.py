"""
  field:
    W : width
    H : height
    state for every x, y
    location with cell and state
"""

import copy
import random as rng

## Constants ##
H = 125   #Height
W = 10   #Width
T = 100  #Number of ticks




"""
For a space that is 'populated':
  Each cell with one or no neighbors dies, as if by solitude.
  Each cell with four or more neighbors dies, as if by overpopulation.
  Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
  Each cell with three neighbors becomes populated.
"""


def get_new_state(states, x, y):

  # TODO: Boundary stuff ....
  neighbours = [states[x+dx][y+dy]
                  for dy in [-1, 0, 1] for dx in [-1, 0, 1]
                  if  not dx==dy==0 # Not the cell itself
                  and 0 <= x+dx < W # Boundary condition horizontal
                  and 0 <= y+dy < H # Boundary condition vertical
                ]
  count_living = sum(neighbours)

  if count_living == 3:
    return True
  if count_living == 2 and states[x][y]: # already alive, lives on
    return True
  return False


## Main access ##

# Random initial
states = [[rng.random()>.5 for y in range(H)] for x in range(W)]

for time in range(T):
  # Find new states
  new_states = [[get_new_state(states, x, y) for y in range(H)] for x in range(W)]
  # Update to the grid
  states = copy.deepcopy(new_states) # syntax ?

  print(H*'-')
  print('\n'.join([''.join([('#' if state else ' ') for state in staterow]) for staterow in states]))