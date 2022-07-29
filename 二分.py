# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 心得：
# 做二分题目的时候要在心里构想出图形化的 mid 向 start 或 end 的逼近状态

# —————— ฅ՞• •՞ฅ ———————
# **没找到 target 的时候 start end 停在哪里？分三种情况

# 1. target 比数组头小的时候，start = 0 end = 1
# 2. target 比数组尾大的时候，start = -2 end = -1
# 3. target 在中间的时候，start 是比 target 小的，end 是比 target 大的，end 位置是插入的地方

# 可看题目 35. 搜索插入位置 https://leetcode.cn/problems/search-insert-position/
# 以上适用于无重复元素的情况


# —————— ฅ՞• •՞ฅ ———————
# **判断里 = 的情况的用处在于：
# 


def binary_search(nums, target):
    # corner case 处理
    # 这⾥等价于 nums is None or len(nums) == 0
    if not nums:
        return -1

    start, end = 0, len(nums) - 1

    # ⽤ start + 1 < end 避免死循环，解释过程略
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

    # 上⾯的循环退出条件是 start + 1 < end
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
def search(self, nums, target) -> int:
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