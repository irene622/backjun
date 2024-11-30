import sys
from collections import deque

N = int(sys.stdin.readline().strip())
result = deque([]) #(num, parent index)
for i in range(N):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if len(result) == 0:
            print(0)
        else:
            print(result.popleft()[0], "h")
    elif len(result) == 0:
        result.append([n,-1])
    else:
        idx_parents = (i-1)//2

        for data in result:
            if data[1] == idx_parents:
                parent = result[idx_parents]
        if parent[0] > n:
            result.append([n, parent[1]])
            parent[1] = (i-1)//2
        else:
            result.append([n, idx_parents])


print(result)