import sys
from collections import deque

# sys.stdin = open('dfsbfs/2178.txt', 'r')
N, M = map(int, sys.stdin.readline().strip().split(' ')) # N=row, M=col
direction = [(1,0),(0,1),(-1,0),(0,-1)]
grid = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[0]*M for _ in range(N)] # 몇번만에 방문했는지.

def search_grid(start):
    next = deque([start])
    num = 0
    visited[start[0]][start[1]] = 1

    while next:
        current_x, current_y = next.popleft() #(0,0)
        for dx, dy in direction:
            x, y = current_x + dx, current_y + dy
            if 0<= x <= N-1 and 0<= y <= M-1 and grid[x][y]=='1' and visited[x][y] == 0:
                next.append((x,y))
                visited[x][y] = visited[current_x][current_y] + 1
                num += 1
                
    print(visited[-1][-1])

search_grid((0,0))




