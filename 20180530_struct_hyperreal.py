"""
Hyperreal numbers as an extension of float

https://en.wikipedia.org/wiki/Hyperreal_number

"""


class HFloat(float):
  """docstring for HFloat"""

  mul_map = {
    'one'    : {'one' : 'one'    , 'omega' : 'omega', 'epsilon' : 'epsilon'},
    'omega'  : {'one' : 'omega'  , 'omega' : 'omega', 'epsilon' : 'one'},
    'epsilon': {'one' : 'epsilon', 'omega' : 'one'  , 'epsilon' : 'epsilon'},
            }

  def __new__(self, value, unit = 'one'): # Float is immutable, so overwrite new as well
    self.unit = unit
    return float.__new__(self, value)

  def __init__(self,value, unit = 'one'):
    super(float, self).__init__()

  def __mul__(self, other):
    if type(other) != HFloat:
      ounit = 'one'
    else:
      ounit = other.unit
    newval = super().__mul__(other)
    newunit = HFloat.mul_map[self.unit][ounit]
    return HFloat(newval, newunit)


  def __truediv__(self, other):
    return super().__truediv__(other)

  def __add__(self, other):
    if not self.unit and not other.unit:
      return

  def __str__(self):
    return super().__str__() + {'omega' : 'ω', 'epsilon' : 'ε', 'one': ''}.get(self.unit, )



f = HFloat(1, unit = 'epsilon')

# print(f.unit)
# print(f)
print(f + 1)
# print(f/2)
# print(f/0)

# print(dir(f))