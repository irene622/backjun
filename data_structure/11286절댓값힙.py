import sys
import heapq

sys.stdin = open("data_structure/ex.txt")
N = int(sys.stdin.readline().strip())

abs_heap = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())

    if num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    else:
        if len(abs_heap) == 0:
            print(0)
        else:
            pop = heapq.heappop(abs_heap)
            print(pop[1])
