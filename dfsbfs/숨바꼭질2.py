import sys
from collections import deque

me, you = map(int, sys.stdin.readline().strip().split(' '))

def bfs(status, goal):
    next = deque([status])
    sec = 0
    num_path = 0

    while next:
        current = next.popleft()
        directions = [current-1, current+1, current*2]
        for i in directions:
            if 0<= i <= 100_000:
                sec += 1
                if i == goal:
                    print(i)
                    if sec < sec: # TODO: 최소시간 경로인걸 어떻게 판단하지?
                        num_path += 1
                    return sec, num_path
                else:
                    next.append(i)

print(bfs(me, you))