# 技巧：模板中两处while root相同

# 在 BST 中，while root的意义在于：比 root 大的最小值位于 root 右子树的最左子树
# 参考下 450. 删除二叉搜索树中的节点 https://leetcode.cn/problems/delete-node-in-a-bst/

def midOrder(self, root):
    stack = []
    result = []
    while root:
        stack.append(root)
        root = root.left
    
    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.right:
            root = root.right
            while root:
                stack.append(root)
                root = root.left
    