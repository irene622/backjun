import sys
from collections import deque

sys.stdin = open('dfsbfs/ex.txt', 'r')
num, lines, starter = map(int, sys.stdin.readline().strip().split(' '))
graph = {i: [] for i in range(1, num + 1)}
dfsvisited = {i: False for i in range(1, num + 1)}
for _ in range(lines):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    if graph.get(a) == None:
        graph[a] = [b]
    else:
        graph[a] += [b]

    if graph.get(b) == None:
        graph[b] = [a]
    else:
        graph[b] += [a]

bfsvisited = {k:v for k,v in dfsvisited.items()}

# def dfs(starter):
#     stack = [starter]  # 스택 사용 # 새롭게 넣은걸 먼저 한다.
#     dfsvisited[starter] = True
#     dfs_path = str(starter)

#     while stack:
#         current = stack.pop()  
#         for i in sorted(graph[current], reverse=True):  
#             if not dfsvisited[i]:
#                 stack.append(i)
#                 if not dfsvisited[current]:
#                     dfs_path += ' ' + str(current)
#                 dfsvisited[current] = True
#     return dfs_path

def dfs(starter):
    dfsvisited[starter] = True
    bfs_path = str(starter)
    for neighbor in sorted(graph[starter]):
        if not dfsvisited[neighbor]:
            bfs_path += ' ' + dfs(neighbor)
    return bfs_path

print(dfs(starter))
# print('')

def bfs(starter):
    queue = deque([starter]) # 넣었던걸 다 하고, 다음 단계로 가겠다.
    bfsvisited[starter] = True
    bfs_path = str(starter)

    while queue:
        current = queue.popleft()
        for i in sorted(graph[current]):
            if not bfsvisited[i]:
                queue.append(i)
                bfsvisited[i] = True
                bfs_path += ' ' + str(i)
    return bfs_path

print(bfs(starter))




