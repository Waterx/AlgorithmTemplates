# quick sort

# 时间复杂度	 
# 最好的	O(n*log n)
# 最差的	O(n 2 )
# 平均	    O(n*log n)

# 空间复杂度	O(log n)
# 稳定	不

# tip: 只要 left 和 right 比较都带等于，（左右带等比四次，
#      和 pivot 比较都不带等于          （派非下标不带等
#      算法结构类似二叉树先序遍历        （先序参数交错开

def sortIntegers(A):
    # Write your code here
    quickSort(A, 0, len(A) - 1)

def quickSort(A, start, end):
    if start >= end:
        return
    left, right = start, end
    # key point 1: pivot是值而不是下标
    pivot = A[(start + end) // 2]

    # key point 2: 每次都要比较 left 和 right ，一共 4 次，并且注意带 = 号
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            
    quickSort(A, start, right)      # key point 3: 最后 left 和 right 会交错开
    quickSort(A, left, end)


def _main():
    arr = [3,2,3,1,4,6]
    sortIntegers(arr)
    print(arr)

_main()