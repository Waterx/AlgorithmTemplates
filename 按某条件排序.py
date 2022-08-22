
# 按元组第2位排序
nums = [(3, 1), (3, 3), (2, 2)]
nums.sort(key = lambda x:x[1])
print(nums)

nums = [(3, 1), (3, 3), (2, 2)]
def second(t):
    return t[1]
nums.sort(key = second)
print(nums)

# 按绝对值排序
nums = [-5, 3, 4, -1]
nums.sort(key = abs)
print(nums)
