import sys
from collections import deque

sys.stdin = open('dfsbfs/ex.txt')
# N=세로길이=num row, M=가로길이=num col, K=num trash
N, M, K = map(int, sys.stdin.readline().strip().split(' ')) 

grid = [[False]*M for _ in range(N)]
for _ in range(K):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    grid[x-1][y-1] = True

visited = [[False]*M for _ in range(N)]

def calcu_size(grid, start):
    stack = deque([start])
    visited[start[0]][start[1]] = True

    if grid[start[0]][start[1]]:
        size = 1
    else:
        size = 0

    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    while stack:
        curr_x, curr_y = stack.popleft() # popleft = bfs
        for dx, dy in directions:
            next_x, next_y = curr_x+dx, curr_y+dy
            if 0 <= next_x < N and 0<= next_y < M:
                if visited[next_x][next_y] is False:
                    if grid[next_x][next_y]:
                        size += 1
                        stack.append((next_x, next_y))
                        visited[next_x][next_y] = True
                    else:
                        visited[next_x][next_y] = True

    return size

cand_size = []
for x in range(N):
    for y in range(M):
        if visited[x][y] is False:
            size = calcu_size(grid, (x,y))
            cand_size.append(size)

print(cand_size)
print(max(cand_size))

