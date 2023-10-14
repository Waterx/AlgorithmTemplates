

# 背向双指针
left = position
right = position + 1
while left >= 0 and right < len(s):
    if left 和 right 可以停下来了:
        break
left -= 1
right += 1



# 同向双指针
j = 0
for i in range(n):
# 不满足则循环到满足搭配为止
    while j < n and i到j之间不满足条件:
        j += 1
    if i到j之间满足条件:
        处理i到j这段区间