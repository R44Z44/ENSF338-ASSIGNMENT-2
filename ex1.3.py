cache = []
for i in range(75):
    cache.append(None)

def func(n, cache):
    if n == 0 or n == 1:
        return n
    if cache[n] != None:
        return cache[n]
    else:
        cache[n] = func(n - 1, cache) + func(n - 2, cache)
        return cache[n]

