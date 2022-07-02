# Python 不提供大顶堆，因此改造小顶堆，包装一下方便刷题用。
# 原理是 push 和 pop 时候都加负号

import heapq

def heapify(self, x):
    for i in range(len(x)):
        x[i] = -x[i]
    heapq.heapify(x)
    return x
def heappush(self, heap, item):
    heapq.heappush(heap, -item)
def heappop(self, heap):
    return -heapq.heappop(heap)
def heapmax(self, heap):
    return -heap[0]