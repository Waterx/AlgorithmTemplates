
# 在 BST 中，while root的意义在于：比 root 大的最小值位于 root 右子树的最左子树
# 参考下 450. 删除二叉搜索树中的节点 https://leetcode.cn/problems/delete-node-in-a-bst/

# 技巧：模板中两处while root组件相同

def midOrder(self, root):
    stack = []
    result = []
    while root: 
        stack.append(root)
        root = root.left
    
    while stack:
        root = stack.pop()
        # 这里相当于递归方法的 dfs(root.left) 与 dfs(root.right) 之间的部分
        result.append(root.val)
        if root.right:
            root = root.right
            while root:
                stack.append(root)
                root = root.left
