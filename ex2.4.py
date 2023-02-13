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

llen = []
quicksort= []
for subarray in d:
    start_time = quicksort.time()

    func1(subarray, 0, len(subarray)-1)
        
    end_time = quicksort.time()

    quicksort.append(end_time - start_time)
    llen.append((str(len(subarray))))

for z in range (0,len(llen)):
    print("time taken for length", llen[z], "is", quicksort[z],"seconds")


print(d[0])

plt.scatter(llen, quicksort)
plt.xlabel("List length")
plt.ylabel("Exec Time")
plt.title('Time vs. List Length')
plt.show()