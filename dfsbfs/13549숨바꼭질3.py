import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))
visited = [0 for _ in range(100_001)]
time = [0 for _ in range(100_001)]

def checktime(start, goal):
    next = deque([start])
    visited[start] = 1

    while next:
        current = next.popleft()

        if current == goal:
            shortest_time = time[goal]
            break

        for i in [current-1, current+1, current*2] :
            if 0<= i <= 100_000 and visited[i] == 0:
                visited[i] = visited[current] + 1
                if i != current*2:
                    time[i] = time[current] + 1
                    next.append(i)
                else:
                    time[i] = time[current]
                    next.appendleft(i)
                
    
    print(shortest_time)

checktime(N, K)