# Example 1 - Generate names from files
from rancat import RanCat

r = RanCat(seed=12335).load('examples/data/jedi.txt')
r.load('examples/data/got.txt')
for i in range(0, 10):
    print(r.next())