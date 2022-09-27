
def findMedian(arr):
    arr.sort()
    median = arr[len(arr) // 2]
    return median


arr = [0, 1, 2, 4, 6, 5, 3]
print(findMedian(arr))
