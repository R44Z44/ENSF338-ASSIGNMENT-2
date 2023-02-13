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
for sublist in d:
    start_time = quicksort.time()

    func1(sublist, 0, len(sublist)-1)
        
    end_time = quicksort.time()

    quicksort.append(end_time - start_time)
    lilen.append((str(len(sublist))))

for z in range (0,len(lilen)):
    print("time taken for length", lilen[z], "is", quicksort[z],"seconds")


print(d[0])

plt.scatter(lilen, quicksort)
plt.xlabel("List length")
plt.ylabel("Exec Time")
plt.title('Time vs. List Length')
plt.show()