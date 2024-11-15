import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))
visited = [0 for _ in range(100_001)] # 방문을 확인할 것이면, visited = [False] * 100_001해도 된다.
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
            if 0<= i <= 100_000 and visited[i] == 0: # visited[i] == visited[current]+1 삭제.. 넣어도 상관없지 않나..?
                visited[i] = visited[current] + 1
                if i != current*2:
                    time[i] = time[current] + 1
                    next.append(i)
                else:
                    time[i] = time[current]
                    next.appendleft(i) # append 아니고 appendleft.
                
    
    print(shortest_time)

checktime(N, K)