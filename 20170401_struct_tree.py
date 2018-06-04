

class Tree():
  """Tree consisting of Nodes"""
  def __init__(self, rootcontent = None):
    self.root = self.Node(rootcontent)

  def breath_first_search(self,content):
    checklist = [self.root]
    while checklist:
      # Check if content is currently in the list
      for c in checklist:
        if c.content == content:
          return c
      # if not: get all children of nodes in the list and update
      new_checklist = [c for cc in checklist for c in cc.children ]
      checklist = new_checklist

  def depth_first_search(self, content):
    return self.root.depth_first_search(content)

  class Node():
    """Node"""
    def __init__(self, content = None):
      self.content = content
      self.children = []

    def __repr__(self):
      return repr(self.content)

    def depth_first_search(self, content):
      if self.content == content:
        return self
      for child in self.children:
        foundnode = child.depth_first_search(content)
        if foundnode:
          return foundnode



# create the tree
tree = Tree('root')
root = tree.root
newnodes = [tree.Node(i) for i in range(3)]
root.children = newnodes
newnodes = [tree.Node(10+i) for i in range(2)]
root.children[1].children = newnodes

# print(tree.root)
# print(tree.root.children)
# for c in tree.root.children:
#   print(c.children)


print(tree.breath_first_search(11))
print(tree.depth_first_search(0))




s = [1,2,3]

for i, k in enumerate(s):
  print(i,k)
  if k ==2:
    s.append(12)
  if k==12:
    s = s+[14]
  # if k ==1:
  #   del(s[0])