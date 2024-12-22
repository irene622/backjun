import sys
import heapq

sys.stdin = open('data_structure/ex.txt')
N = int(sys.stdin.readline().strip())
heap = []
for i in range(N):
    numbers = map(int, sys.stdin.readline().strip().split())

    if i == 0:
        for num in numbers:
            heapq.heappush(heap, num)
    else:
        for num in numbers:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
