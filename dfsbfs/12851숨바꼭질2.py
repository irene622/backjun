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
            continue

        directions = [current-1, current+1, current*2]
        for i in directions:
            # 범위에 있는지.
            # 빠른 경로로 온 경우에 체크. 1-2-3-2는 반복하기에 제외.. 5-4-3-6는 5-6이 더 빠른 경로이기 때문에 5-4-3-6은 제외.
            # visited[i] == visited[current] + 1. current의 depth와 i의 depth를 생각. 
            #     i의 depth에서 조사하고자 하는 i가 중복되도 조사한다. 3-4-5와 3-6-5모두 조사해야 다른 경로임을 카운트할 수 있다.
            if 0<= i <= 100_000 and (visited[i] == 0 or visited[i] == visited[current] + 1):
                visited[i] = visited[current] + 1
                next.append(i)

    print(sec)
    print(num_path)
    return num_path, sec

bfs(me, you)
