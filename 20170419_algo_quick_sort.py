

# Pick pivot

# Partition in lower and higher part

# Recursively sort lower and higher


def quicksort(in_list):

  if len(in_list)<2:
    return in_list

  pivot_index = int(len(in_list)/2) #choice of pivot?
  pivot_val = in_list[pivot_index]

  # in place?
  lower_list  = [val for i,val in enumerate(in_list) if val<=pivot_val and i!= pivot_index]
  higher_list = [val for   val in in_list            if val>pivot_val]

  return quicksort(lower_list) + [pivot_val] + quicksort(higher_list)


import random
print(quicksort([random.randint(0,10) for i in range(10)]))