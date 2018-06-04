import bisect

class linterpol(object):
  """docstring for linterpol"""
  def __init__(self, keyval_pairs = None):
    self.x_list = []  # Sorted
    self.y_list = []

    if keyval_pairs:
      for key, val in keyval_pairs:
        self[key] = val

  def __call__(self, key):
    # Error for zero keys
    if len(self.x_list) == 0:
      raise KeyError('No key/value pairs defined')
    # Constant for one key
    if len(self.x_list) == 1:
      return self.y_list[0]
    index_right = min(bisect.bisect_left(self.x_list,key), len(self)-1)
    index_left = index_right-1
    # Interpolate
    key_left, key_right = self.x_list[index_left], self.x_list[index_right]
    weight_left, weight_right = (key_right-key)/(key_right-key_left), (key-key_left)/(key_right-key_left)
    return (self.y_list[index_left]*weight_left + self.y_list[index_right]*weight_right)


  def __setitem__(self, key, value):
    # Find insertion point
    insertion_index = bisect.bisect_left(self.x_list,key)
    if insertion_index < len(self) and self.x_list[insertion_index] == key:
      #override
      self.y_list[insertion_index] = value
    else:
      # Insert into key and value array.
      self.x_list[insertion_index:insertion_index] = [key]
      self.y_list[insertion_index:insertion_index] = [value]

  def __len__(self):
    return len(self.x_list)

  def __delitem__(self, key):
    key_index = self.x_list.index(key)
    del(self.x_list[key_index])
    del(self.y_list[key_index])

  def __repr__(self):
    return ', '.join(['{}:{}'.format(k,v) for k,v in self.get_pairs()])

  def get_pairs(self):
    return zip(self.x_list, self.y_list)

  def get_intervals(self):
    x_intervals = (t - s for s, t in zip(self.x_list, self.x_list[1:]))
    y_intervals = (t - s for s, t in zip(self.y_list, self.y_list[1:]))
    return zip(x_intervals, y_intervals)

  def get_sq_distances(self):
    return (x_int**2 + y_int**2 for x_int, y_int in self.get_intervals())

  def get_slopes(self):
    # Approximate derivative
    return (y_int/x_int for x_int, y_int in self.get_intervals())

  def get_trapezoidal_sum(self, lower = 0, upper = None):
    # Approximate integral
    if not upper:
      upper = len(self)
    trap_sum = 0
    intervals = list(self.get_intervals())
    for i in range(lower, upper-1):
      delta_x = intervals[i][0]
      trap_sum += delta_x * (self.y_list[i] + self.y_list[i+1])/2
    return trap_sum


  def prune_dense_nodes(self, min_dist):
    sq_dists = list(self.get_sq_distances())
    node_is_dense = lambda i: sq_dists[i-1] < min_dist**2 and sq_dists[i] < min_dist**2
    dense_indices = [i for i in range(1, len(self)-1) if node_is_dense(i) and i%2==1] # only prune odd nodes
    self.x_list = [x for i, x in enumerate(self.x_list) if i not in dense_indices]
    self.y_list = [y for i, y in enumerate(self.y_list) if i not in dense_indices]
    if dense_indices:
      self.prune_dense_nodes(min_dist)



class linterpol_dict(dict):
  """docstring for linterpol_dict"""
  def __init__(self):
    super(linterpol_dict, self).__init__()
    self.x_list = []  # Sorted keys

  def __call__(self, key):
    # Error for zero keys
    if len(self.x_list) == 0:
      raise KeyError('No key/value pairs defined')
    # Constant for one key
    if len(self.x_list) == 1:
      return self[self.x_list[0]]
    index_right = min(bisect.bisect_left(self.x_list,key), len(self)-1)
    index_left = index_right-1
    # Interpolate
    key_left, key_right = self.x_list[index_left], self.x_list[index_right]
    weight_left, weight_right = (key_right-key)/(key_right-key_left), (key-key_left)/(key_right-key_left)
    value_left, value_right = self[self.x_list[index_left]], self[self.x_list[index_right]]
    return (value_left*weight_left + value_right*weight_right)

  def __setitem__(self, key, value):
    # Insert key into sorted array
    insertion_index = bisect.bisect_left(self.x_list,key)
    if insertion_index < len(self) and self.x_list[insertion_index] == key:
      #override
      pass
    else:
      # Insert into key array
      self.x_list[insertion_index:insertion_index] = [key]

    # Add value
    super().__setitem__(key, value)

  def __delitem__(self, key):
    key_index = self.x_list.index(key)
    del(self.x_list[key_index])
    super().__delitem__(key)

  def items(self):
    # Sorted output
    return ([k, self[k]] for k in self.x_list)

  def get_intervals(self):
    items = list(self.items())
    x_intervals = (t - s for s, t in zip(self.x_list, self.x_list[1:]))
    y_intervals = (t - s for s, t in zip(self.y_list, self.y_list[1:]))
    return zip(x_intervals, y_intervals)

  def get_sq_distances(self):
    return (x_int**2 + y_int**2 for x_int, y_int in self.get_intervals())

  def get_slopes(self):
    # Approximate derivative
    return (y_int/x_int for x_int, y_int in self.get_intervals())


li = linterpol_dict()

li[0] = 0
li[1] = 1

print(li[1])
print(li(.2))

del(li[0])
print(li)

print(list(li.items()))

# exit()


from math import sin
import random as rng
import matplotlib.pyplot as plt


li = linterpol()
for i in range(10000):
  x = 2*rng.random() + .001
  y = sin(1/x)
  li[x] = y

print(len(li))
li.prune_dense_nodes(.01)
print(li.x_list[-10:])
fig, ax = plt.subplots()

# plt.grid(False)
# plt.axis('off')

ax.plot(li.x_list,li.y_list)
plt.show()
