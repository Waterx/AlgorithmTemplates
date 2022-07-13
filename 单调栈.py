
stack = []
for i in range(nums):

    while stack and stack[-1] > nums[i]:
        stack.pop()
    
    stack.append(nums[i])
    