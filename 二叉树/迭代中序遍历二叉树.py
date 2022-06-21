# 技巧：模板中两处while root相同

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
    