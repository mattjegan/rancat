# The RanCat Object

## RanCat (class)
### RanCat(seed=None, unique=False, read_size=1000) 
*returns RanCat*

Initializes the RanCat object with an optional keyword arguments:

* **seed**: A seed for the random generator.
* **unique**: A boolean that will force unique phrases until no more combinations are possible.
* **read_size**: The number of units for RanCat to read when loading from sources. The default of 1000 keeps execution time down while still allowing for ~1 million unique phrases given 2 text sources of 1000+ units.

```python
from rancat import RanCat

r = RanCat()
r = RanCat(seed=123)
r = RanCat(unique=True)
r = RanCat(read_size=5)
```

### RanCat.load(filepath)
*returns RanCat*

[Semi-lazily loads](https://thedevmatt.wordpress.com/2016/08/12/semi-lazy-loading-in-rancat/) a data source into RanCat. The data source may be any:

* Filepath (string)
* List
* Tuple

```python
r = RanCat()
r.load('path/to/file.txt')
r.load(['cat', 'dog'])
r.load(('cat', 'dog'))
```

### RanCat.next()
*returns string*

Generates and returns the next phrase from the loaded sources.

```python
r = RanCat()
r.load(['the', 'a']).load(['dog', 'cat'])
r.next()
>>> 'the_dog'
```

### RanCat.soft_reset()
*returns RanCat*

Clears all tracking of seen phrases. This can be used when **unique** is set to True and RanCat has exhausted all combinations.

```python
r = RanCat(unique=True)
r.load(['word1', 'word2'])
r.next()
r.next()

# All phrases have been used
r.soft_reset()

# And now we can start calling next() again
r.next()
r.next()
```

### RanCat.hard_reset()
*returns None*

Performs *RanCat.soft_reset()* and also clears the loaded sources.

```python
r = RanCat()
r.load(['cat', 'dog'])   # The array is now stored for use by RanCat.next()
r.hard_reset()           # The array is now not available for use by RanCat.next()
r.load(['new', 'array']) # This new array is the only source available by RanCat.next()
```

### RanCat.set_conversion(conversion_callable)
*returns RanCat*

Takes a callable which accepts a two strings as parameters:

* **phrase**: A unit from a data source.
* **sep**: A separator that may be used in the callable.

See *Conversions* for some pre-written callables.

```python
from rancat.conversions import ascii_lower

r = RanCat()
r.set_conversion(ascii_lower)
```

### RanCat.set_unique(boolean)
*returns RanCat*

Sets the uniqueness property, boolean should be:

* **True**: All phrases will be unique
* **False**: Phrases are not necessarily unique

```python
r = RanCat()
r.set_unique(True)
```

### RanCat.set_read_size(read_size)
*returns RanCat*

Sets the read size of the data sources. The default is 1000 units. A unit may be a line in a file or a value at some index in a list or tuple.

```python
r = RanCat()
r.set_read_size(5000)
```

### RanCat.set_separator(sep)
*returns RanCat*

Sets the value of the separator to be used in generating phrases. The default is the underscore `_`. This value is not only used to join units together but is also passed to the conversion method for various uses such as substitution of certain characters.

```python
r = RanCat()
r.set_separator(' ') # RanCat will now use spaces between units
```

### RanCat.load_structure(*args)
*returns RanCat*

Similar to *RanCat.load()* but can take multiple data sources.

```python
r = RanCat()
r.load_structure('path/to/file.txt', ['the', 'a'], ('dog', 'cat'), ['!']) # Loads all 4 sources into RanCat
``` 

