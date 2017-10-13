# Welcome to RanCat
Master
[![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=master)](https://travis-ci.org/mattjegan/rancat) [![codecov](https://codecov.io/gh/mattjegan/rancat/branch/master/graph/badge.svg)](https://codecov.io/gh/mattjegan/rancat) [![PyPI version](https://badge.fury.io/py/rancat.svg)](https://badge.fury.io/py/rancat) [![Documentation Status](https://readthedocs.org/projects/rancat/badge/?version=latest)](http://rancat.readthedocs.io/en/latest/?badge=latest)

Develop
[![Build Status](https://travis-ci.org/mattjegan/rancat.svg?branch=develop)](https://travis-ci.org/mattjegan/rancat) [![codecov](https://codecov.io/gh/mattjegan/rancat/branch/develop/graph/badge.svg)](https://codecov.io/gh/mattjegan/rancat)

This is the full documentation of [RanCat](https://github.com/mattjegan/rancat), an open source Python **Ran**dom con**Cat**enation engine.

## Use Cases

RanCat is a string generator that can use multiple text sources, including files and native Python lists and tuples. What constitutes a word in a word list is simply an atomic entity in the source, e.g. a line in a file, or a value in a list. RanCat will generate pseudo-random strings that are suitable for use as :

* VCS Branch Names
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

# Contributing

## Submitting an issue or feature request

If you find an issue or have a feature request please open an issue at [Github RanCat Repo](https://github.com/mattjegan/rancat).

## Working on issues

If you think that you can fix an issue or implement a feature, please make sure that it isn't assigned to someone or if it is you may ask for an update.

Once an issue is complete, open a pull request so that your contribution can be reviewed. A TravisCI build and CodeCov report will run and be attached to your pull request. Your code must pass these checks.

## Helping others

At all times, please be polite with others who are working on issues. It may be their first ever patch and we want to foster a friendly and familiar open source environment.
