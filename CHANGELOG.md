# RanCat 1.0.0
* Allows custom phrase structure via `RanCat().load_structure(*args)` where args are either filepaths (str) or iterables of strings (tuples, lists)

# RanCat 0.0.3

* Allows use of own conversion function via `RanCat().set_convert_func(FUNC)`
* Allows use as an iterator `for x in <rancat instance>: ...`
* Allows uniqueness to be guarenteed through `RanCat(unique=True)` or `RanCat().set_unique(True)`, defaults to False
* Allows chaining of some commands, `RanCat().set_unique(True).set_convert_func(FUNC).load(...).load(...)`
* Files are now semi-lazily evaluated, iterative read size can be set via `RanCat(read_size=num_lines)` or `RanCat().set_read_size(num_lines)`
* Allows the use of the same datafile multiple times
* Supports `RanCat().soft_reset()` which will reset the combinations being produced but not the files being used.
* Supports `RanCat().hard_reset()` which performs a soft reset as well as resetting all files being used.