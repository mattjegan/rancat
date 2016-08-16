# Example 2 - Generate phrases from iterables
from rancat import RanCat

r = RanCat(seed=12335)
r.load_structure(['the'], ['cat', 'dog'], ['was'], ['black', 'brown'])
print(r.next())