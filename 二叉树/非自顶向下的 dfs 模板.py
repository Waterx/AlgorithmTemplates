# https://leetcode.cn/problems/diameter-of-binary-tree/solution/yi-pian-wen-zhang-jie-jue-suo-you-er-cha-6g00/

# 124. 二叉树中的最大路径和 
# 687. 最长同值路径 
# 543. 二叉树的直径

# ignore this
class TreeNode:
    pass
root = TreeNode()


# the template begins here

max_value = 0
def find_max(root):
    if not root:
        return 0
    left = find_max(root.left)
    right = find_max(root.right)
    max_value = max(max_value, left + right + root.val)
    return max(left, right)

# end