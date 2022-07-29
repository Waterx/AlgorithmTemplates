# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 心得：
# 做二分题目的时候要在心里构想出图形化的 mid 向 start 或 end 的逼近状态



def binary_search(nums, target):
    # corner case 处理
    # 这⾥等价于 nums is None or len(nums) == 0
    if not nums:
        return -1

    start, end = 0, len(nums) - 1

    # ⽤ start + 1 < end ⽽不是 start < end 的⽬的是为了避免死循环
    # 在 first position of target 的情况下不会出现死循环
    # 但 last position of target 的情况下会出现死循环
    # 样例：nums=[1，1] target = 1
    # 为了统⼀模板，我们就都采⽤ start + 1 < end，就保证不会出现死循环
    while start + 1 < end:
        # python 没有 overflow 的问题，直接 // 2 就可以了
        mid = (start + end) // 2
        # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分⽀⾥
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid   

    # 因为上⾯的循环退出条件是 start + 1 < end
    # 因此这⾥循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
    # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
    # 如果是找 first position of target 就先看 start，否则就先看 end
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1

A = [1,2,3,4,5,8,9]
print(binary_search(A, 1))
print(binary_search(A, 3))
print(binary_search(A, 8))



#  ************ 去掉注释版本 *********************
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid
        elif target == nums[mid]:
            end = mid
        else:
            start = mid
    
    if nums[start] == target:
        return start 
    if nums[end] == target:
        return end
    
    return -1