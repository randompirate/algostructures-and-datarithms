


## [2,1,3,4]
## Split [2,1] [3,4]
  ## Sort: [2,1]
  ## Split: [2], [1]
    ## Sort [2]: Base
    ## Sort [1]: Base
  ## Merge:
    ## retlist = []
    ## [1]
    ## While fails:
    ## [1, 2]

def merge_sort(list_in):

  # Base case
  if len(list_in) in [1,0]:
    return list_in

  #Split in half
  half_index = int(len(list_in)/2)
  listA, listB = list_in[:half_index], list_in[half_index:]

  # Sort listA and listB recursively:
  listA = merge_sort(listA)
  listB = merge_sort(listB)

  # Merge back
  retlist = []
  while listA and listB:
    if listA[0]<=listB[0]:
      retlist.append(listA[0])  # something like .pop()?
      del(listA[0])
    else:
      retlist.append(listB[0])
      del(listB[0])

  retlist = retlist + listA + listB   # at least one of them is empty
  return retlist


import random
print(merge_sort([random.randint(0,100) for i in range(10)]))