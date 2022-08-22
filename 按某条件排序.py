
# 按元组第2位排序
nums = [(3, 1), (3, 3), (2, 2)]
nums.sort(key = lambda x:x[1])
print(nums)

nums = [(3, 1), (3, 3), (2, 2)]
def second(t):
    return t[1]
nums.sort(key = second)
print(nums)


# 0元素降序，1元素升序
nums = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
def sortRule(nums):
    return -nums[0], nums[1]
nums.sort(key=sortRule)
print(nums)


# 按绝对值排序
nums = [-5, 3, 4, -1]
nums.sort(key = abs)
print(nums)
