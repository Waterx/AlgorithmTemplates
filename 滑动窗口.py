s = "source"
t = "target"

def main():

    left, right = 0, 0
    result = 0

    # right 右滑 扩大窗口
    while right < len(s):
        window.add(s[right])
        right += 1
        # 如果符合要求，移动 left 缩小窗口
        while check(window):
             # 如果这个窗口的子串更短，则更新 res
            result = min(result, len(window))
            window.remove(s[left])
            left += 1

    return result