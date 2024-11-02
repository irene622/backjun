import sys
from collections import deque

num = int(sys.stdin.readline().strip())
RGB_grid = [sys.stdin.readline().strip() for _ in range(num)]
visited = [[False]*num for _ in range(num)]
num_RGB_region = 0
direction = [(1,0),(0,1),(-1,0),(0,-1)] # 근접을 사방으로 확인해서 같은 영역인지 확인한다.
def check_region(grid, x, y):
    visited[x][y] = True
    status = grid[x][y]
    next = deque([(i,j)])
    
    while next:
        x, y = next.popleft()
        for dx,dy in direction:
            if 0<= x+dx <= num-1 and 0<= y+dy <= num-1:
                if not visited[x+dx][y+dy] and grid[x+dx][y+dy] == status:
                    visited[x+dx][y+dy] = True
                    next.append((x+dx, y+dy))

for i in range(num):
    for j in range(num):
        if not visited[i][j]:
            check_region(RGB_grid, i, j)
            num_RGB_region += 1

RB_grid = [line.replace('G', 'R') for line in RGB_grid]
visited = [[False]*num for _ in range(num)]
num_RB_region = 0
for i in range(num):
    for j in range(num):
        if not visited[i][j]:
            check_region(RB_grid, i, j)
            num_RB_region += 1

print(num_RGB_region, num_RB_region)