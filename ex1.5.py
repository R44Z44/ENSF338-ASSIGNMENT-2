import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

cache = []
for i in range(75):
    cache.append(None)

def func_m(n, cache):
    if n == 0 or n == 1:
        return n
    if cache[n] != None:
        return cache[n]
    else:
        cache[n] = func_m(n - 1, cache) + func_m(n - 2, cache)
        return cache[n]

original_time = []
memoization_time = []

for i in range(36):
    start_time = timeit.default_timer()
    func(i)
    original_time.append(timeit.default_timer() - start_time)
    
    start_time = timeit.default_timer()
    func_m(i)
    memoization_time.append(timeit.default_timer() - start_time)

plt.plot(range(36), original_time, label='Original code')
plt.plot(range(36), memoization_time, label='Memoization code')
plt.legend()
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.title('Comparison of original code and memoization code performance')
plt.show()
