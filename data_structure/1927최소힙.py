import sys
from collections import deque

N = int(sys.stdin.readline().strip())
heap = [] # append number. its index is parents order
for i in range(N):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0], "h")
    else:
        # heap push
        heap.append(n)
        current = len(heap) - 1
        while current > 0 :
            parent = (current - 1)//2
            if heap[parent] > heap[current]:
                heap[parent], heap[current] = heap[current], heap[parent]
                current = parent
            else:
                break
    print(heap)