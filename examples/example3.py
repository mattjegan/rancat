# Example 3 - Generate phrases from iterables and files
from rancat import RanCat

r = RanCat(seed=12335)
r.load_structure('examples/data/got.txt', 
    ['is a'], 'examples/data/colors.txt', 
    'examples/data/jedi.txt')
print(r.next())