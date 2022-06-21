import collections

# 二叉树 层序遍历简单模板
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        # do something
        for _ in range(len(queue)):
            node = queue.popleft()
            # do something
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # do something
    return result


def bfs(start_node):

    # BFS 必须要⽤队列 queue，别⽤栈 stack！
    # distance(dict) 有两个作⽤：
    # 1.记录⼀个点是否被丢进过队列了，避免重复访问
    # 2.记录 start_node 到其他所有节点的最短距离

    # 如果只求连通性的话，可以换成 set 就⾏
    # node 做 key 的时候⽐较的是内存地址
    queue = collections.deque([start_node])
    distance = {start_node: 0}

    # while 队列不空，不停的从队列⾥拿出⼀个点，拓展邻居节点放到队列中
    while queue:
        node = queue.popleft()
        # 如果有明确的终点可以在这⾥加终点的判断
        if node 是终点:
            break or return something
        for neighbor in node.get_neighbors():
            if neighor in distnace:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + 1

    # 如果需要返回所有点离起点的距离，就 return hashmap
    return distance
    # 如果需要返回所有连通的节点, 就 return HashMap ⾥的所有点
    return distance.keys()
    # 如果需要返回离终点的最短距离
    return distance[end_node]