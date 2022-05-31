# quick sort

# 时间复杂度	 
# 最好的	O(n*log n)
# 最差的	O(n 2 )
# 平均	    O(n*log n)

# 空间复杂度	O(log n)
# 稳定	不


def sortIntegers(A):
    # Write your code here
    quickSort(A, 0, len(A) - 1)

def quickSort(A, start, end):
    if start >= end:
        return
    left, right = start, end
    # key point 1: pivot是值而不是下标
    pivot = A[(start + end) // 2]
    # key point 2: 每次都要比较 left 和 right ，并且注意带 = 号
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    quickSort(A, start, right)
    quickSort(A, left, end)


def _main():
    arr = [3,2,3,1,4,6]
    sortIntegers(arr)
    print(arr)

_main()