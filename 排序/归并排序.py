# MergeSort in Python

# 时间复杂度	 
# 最好的	O(n*log n)
# 最差的	O(n*log n)
# 平均	    O(n*log n)

# 空间复杂度	O(n)
# 稳定	     Yes

def sortIntegers(A):
    if not A:
        return A
    temp = [0] * len(A)
    merge_sort(A, 0, len(A) - 1, temp)


def merge_sort(A, start, end, temp):
    if start >= end:
        return

    # 处理左半区间
    merge_sort(A, start, (start + end) // 2, temp)
    # 处理右半区间
    merge_sort(A, (start + end) // 2 + 1, end, temp)
    # 合并排序数组
    merge(A, start, end, temp)


def merge(A, start, end, temp):
    middle = (start + end) // 2
    left_index = start
    right_index = middle + 1
    index = start

    while left_index <= middle and right_index <= end:
        if A[left_index] < A[right_index]:
            temp[index] = A[left_index]
            index += 1
            left_index += 1
        else:
            temp[index] = A[right_index]
            index += 1
            right_index += 1

    while left_index <= middle:
        temp[index] = A[left_index]
        index += 1
        left_index += 1

    while right_index <= end:
        temp[index] = A[right_index]
        index += 1
        right_index += 1
        
    for i in range(start, end + 1):
        A[i] = temp[i]


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 1, 10, 9, 1]
    sortIntegers(array)
    print("Sorted array is: ")
    print(array)