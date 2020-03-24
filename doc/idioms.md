# Tips and tricks #

## Sort a dictionary by keys or values ##

``` python-console
>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
>>> sorted(xs.items(), key=lambda x: x[0])
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]
>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

## Merge two dictionaries ##

``` python-console
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> print({**x, **y})
{'a': 1, 'b': 3, 'c': 4}
>>> print({**y, **x})
{'b': 2, 'c': 4, 'a': 1}
```
