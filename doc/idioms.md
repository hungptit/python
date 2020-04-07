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

## Parameter pack ##

``` python
args = (1, 2, 3)
dict = {'a': 1, 'b': 2, 'c': 3}

def func(a: int, b : int, c: int):   
     print(a,b,c)

func(*args)
func(**dict)

```

## How to benchmark a small bits of Python code  ##

``` python
import timeit

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print("join:", t)

t = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print("map:", t)

```
