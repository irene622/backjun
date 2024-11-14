import sys
from collections import deque

me, you = map(int, sys.stdin.readline().strip().split(' '))
visited = [0] * 100_001

def bfs(status, goal):
    next = deque([status])
    sec = 0
    num_path = 0

    while next:
        current = next.popleft()

        if current == goal:
            num_path += 1
            sec = visited[current]

        directions = [current-1, current+1, current*2]
        for i in directions:
            if 0<= i <= 100_000 and (visited[i] == 0 or visited[i]== visited[current] +1): #(visited[i] == 0 or visited[i]== visited[current] +1)?
                visited[i] = visited[current] + 1
                next.append(i)
    print(sec)
    print(num_path)
    return num_path, sec

bfs(me, you)