import sys
import json
import timeit
from matplotlib import pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.2.json", "w") as file:
    d = json.load(file)

lilen = []
quicksort= []

for x in d:
    lilen = len(x)
    elaspedTime = timeit.timeit(lambda : func1(x, 0, (lilen - 1) ), n= 1)
    quicksort.append(elaspedTime)
    lilen.append(lilen)

plt.plot(lilen, quicksort)
plt.xlabel("List length")
plt.ylabel("Exec Time")
plt.show()