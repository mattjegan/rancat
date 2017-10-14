# Welcome to RanCat
Master
[![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=master)](https://travis-ci.org/mattjegan/rancat) [![codecov](https://codecov.io/gh/mattjegan/rancat/branch/master/graph/badge.svg)](https://codecov.io/gh/mattjegan/rancat) [![Code Health](https://landscape.io/github/mattjegan/rancat/master/landscape.svg?style=flat)](https://landscape.io/github/mattjegan/rancat/master) [![PyPI version](https://badge.fury.io/py/rancat.svg)](https://badge.fury.io/py/rancat) [![Documentation Status](https://readthedocs.org/projects/rancat/badge/?version=latest)](http://rancat.readthedocs.io/en/latest/?badge=latest)

Develop
[![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=develop)](https://travis-ci.org/mattjegan/rancat) [![codecov](https://codecov.io/gh/mattjegan/rancat/branch/develop/graph/badge.svg)](https://codecov.io/gh/mattjegan/rancat) [![Code Health](https://landscape.io/github/mattjegan/rancat/develop/landscape.svg?style=flat)](https://landscape.io/github/mattjegan/rancat/develop)

This is the full documentation of [RanCat](https://github.com/mattjegan/rancat), an open source Python **Ran**dom con**Cat**enation engine.

## Use Cases

RanCat is a string generator that can use multiple text sources, including files and url and native Python lists and tuples. What constitutes a word in a word list is simply an atomic entity in the source, e.g. a line in a file, or a value in a list. RanCat will generate pseudo-random strings that are suitable for use as :

* CVS Branch Names
* Database Names
* Project/Repository Names
* Online Avatar Names
* Baby Names
* and so on

## Installation

```bash
pip install rancat
```

## Basic Usage

```python
from rancat import RanCat

r = RanCat()

# Load in our text sources
r.load(['red', 'orange', 'blue'])
r.load(['car', 'tractor', 'truck'])

# Generate a new string
r.next()
>>> orange_truck
r.next()
>>> red_tractor
r.next()
>>> orange_tractor
```
