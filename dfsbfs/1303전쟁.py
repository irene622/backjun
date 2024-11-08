import sys
from collections import deque

sys.stdin = open('dfsbfs/1303.txt', 'r')
col, row = map(int, sys.stdin.readline().strip().split(' ')) # 가로크기 = 세로줄수, 세로크기 = 가로줄수
grid = []
for i in range(row):
    grid.append(sys.stdin.readline().strip())

directions = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False]*col for _ in range(row)]
def bfs(grid, now_x, now_y):
    w_num, b_num = 0, 0
    color = grid[now_x][now_y]
    visited[now_x][now_y] = True # 방문함
    next = deque([(now_x,now_y)])

    if color == 'W':
        w_num += 1
    else:
        b_num += 1

    while next:
        x, y = next.popleft()
        for i, j in directions:
            dx, dy = x+i, y+j
            if 0 <= dx < row and 0 <= dy < col:
                if color == grid[dx][dy] and visited[dx][dy] == False:
                    visited[dx][dy] = True
                    if color == 'W':
                        w_num += 1
                    else:
                        b_num += 1
                    next.append((dx,dy))       
    return w_num, b_num

    
w_num, b_num = 0,0 
for i in range(row):
    for j in range(col):
        if visited[i][j] == False:
            num = bfs(grid, i, j)
            w_num += num[0]**2
            b_num += num[1]**2

print(w_num, b_num)
