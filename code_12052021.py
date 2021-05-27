import timeit

#Memorization technique in python

def fab(n,cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    result = fab(n - 1, cache) + fab(n - 2, cache)
    cache[n]= result
    print(result)
    return result

print(timeit.timeit('fab(30)',number=100,globals=globals()))


