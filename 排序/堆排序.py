# Heap Sort in python

# 时间复杂度	 
# 最好的	O(nlog n)
# 最差的	O(nlog n)
# 平均	    O(nlog n)

# 空间复杂度	O(1)
# 稳定	不

# 该示例为大顶堆
def heapify(arr, n, i):   #  n代表size  i代表要想让它下沉的下标
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

  
def heapSort(arr):
    n = len(arr)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)
  
  
arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')
