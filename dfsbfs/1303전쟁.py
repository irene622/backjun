import sys
from collections import deque

sys.stdin = open('dfsbfs/1303.txt', 'r')
row, col = map(int, sys.stdin.readline().strip().split(' '))
grid = []
for i in range(row):
    grid.append(sys.stdin.readline().strip())

directions = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False]*col for _ in range(row)]
print(grid)
print('----')
print(visited)
print('---')
def bfs(grid, x, y):
    w_num, b_num = 0, 0
    color = grid[x][y]
    visited[x][y] = '1' # 방문함
    next = deque([(x,y)])

    if color == 'W':
        w_num += 1
    else:
        b_num += 1

    while next:
        for i, j in directions:
            x, y = next.popleft()
            dx, dy = x+i, y+j
            if 0 <= dx < col and 0 <= dy < row:
                if color == grid[dx][dy] and visited[dx][dy] == False:
                    visited[dx][dy] = '1'
                    if color == 'B':
                        w_num += 1
                    else:
                        b_num += 1
                    next.append((dx,dy))       
    return w_num, b_num

    

for i in range(row):
    for j in range(col):
        if visited[i][j] == False:
            num = bfs(grid, i, j)
            print(num)


