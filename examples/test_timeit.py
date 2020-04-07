import timeit

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print("join:", t)

t = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print("map:", t)
