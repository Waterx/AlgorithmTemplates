# MergeSort in Python

# 时间复杂度	 
# 最好的	O(n*log n)
# 最差的	O(n*log n)
# 平均	    O(n*log n)

# 空间复杂度	O(n)
# 稳定	     Yes

def mergeSort(array):
    if len(array) > 1:

        # mid is the point where the array is divided into two subarrays
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        # print(L, R)
        # Sort the two halves
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Until we reach either end of either L or R, pick larger among
        # elements L and R and place them in the correct position at A[p..r]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # When we run out of elements in either L or R,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 1, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)