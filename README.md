# RanCat

Master

[![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=master)](https://travis-ci.org/mattjegan/rancat) [![Coverage Status](https://coveralls.io/repos/github/mattjegan/rancat/badge.svg?branch=master)](https://coveralls.io/github/mattjegan/rancat?branch=master) [![Code Health](https://landscape.io/github/mattjegan/rancat/master/landscape.svg?style=flat)](https://landscape.io/github/mattjegan/rancat/master)
 [![PyPI version](https://badge.fury.io/py/rancat.svg)](https://badge.fury.io/py/rancat)
 
 Develop
 
 [![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=develop)](https://travis-ci.org/mattjegan/rancat) [![Coverage Status](https://coveralls.io/repos/github/mattjegan/rancat/badge.svg?branch=develop)](https://coveralls.io/github/mattjegan/rancat?branch=develop) 
 [![Code Health](https://landscape.io/github/mattjegan/rancat/develop/landscape.svg?style=flat)](https://landscape.io/github/mattjegan/rancat/develop)


RanCat is a string generator that can use multiple text files (word lists) as sources. What constitutes a word in a word list is simply a line in the file. RanCat will generate pseudo-random strings that are suitable for use as github branch names, database names, project names, and so on. The generated names are strings which contain no whitespace.

## Installation

```bash
pip install rancat
```

## Usage

```python
>>> from rancat import RanCat
>>>
>>> r = RanCat() # Takes an optional `seed` parameter
>>>
>>> # Load in our source files
>>> r.load('/path/to/listfile1')
>>> r.load('/path/to/listfile2')
>>>
>>> # Generate a new string
>>> r.next()
orange_truck
>>> r.next()
red_tractor
>>> r.next()
orange_tractor
```

## Source File Rules

An example source file is:

```
orange
lilac purple
y'ellow
```

The rules that are applied are:

* Any trailing whitespace is truncated
* Spaces are converted to underscores
* Hyphens are converted to underscores
* Apostrophes are converted to nothing

## Contributing

If you feel like there is any extra features that users may benefit from please feel free to open a pull request or an issue.

