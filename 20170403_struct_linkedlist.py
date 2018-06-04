

class Llist():
  """Single llist."""
  def __init__(self, content = None, child = None):
    self.content = content
    self.child = child

  def __repr__(self):
    if self.child:
      return str(self.content) + ' > ' + str(self.child)
    return str(self.content)

  # def __len__(self):
  #   if self.child:
  #     return 1 + len(self.child)
  #   return 1

  def __getitem__(self, index):
    if index == 0:
      return self
    return self.child[index-1]

  def __iter__(self):
    # return self
    yield self.content
    if self.child:
      yield from self.child

  def __next__(self):
    return self.child

  def last(self):
    if not self.child:  # it is the last
      return self
    return self.child.last()



def list_to_linkedlist(in_list):
  root = cur_llist = Llist(in_list[0])
  for item in in_list[1:]:
    cur_llist.child = Llist(item)
    cur_llist = cur_llist.child
  return root


def insert_at_index(rootllist, newllist, index):
  """ Insert newllist in the llist following rootllist such that newllist is at the provided index in the resulting llist"""

  # At start
  if index == 0:
    newllist.child = rootllist
    return newllist

  # Walk through the list
  curllist = rootllist
  for i in range(index-1):
    curllist = curllist.child

  # Insert
  newllist.last().child=curllist.child
  curllist.child=newllist

  return rootllist

def test_loop(root):
  # run = True
  single = root
  double = root
  while True:
    single = next(single)
    double = next(double)
    if not single or not double:
      return False
    double = next(double)
    if single == double:
      return True
  # return False


if __name__ == '__main__':

  # llist from list
  root = list_to_linkedlist('a b c d e'.split())
  print(root)

  # insert llist into existing one
  insertion = list_to_linkedlist(['~', '-'])
  root = insert_at_index(root, insertion, 2)
  print(root)

  # get by index
  print(root[3])

  # get last elmnt
  print(root.last())

  # # find loop
  print(test_loop(root))
  root.child.child.child = root.child
  print(test_loop(root))
