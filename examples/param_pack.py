args = (1, 2, 3)
dict = {'a': 1, 'b': 2, 'c': 3}


def func(a: int, b: int, c: int):
    print(a, b, c)


func(*args)
func(**dict)
