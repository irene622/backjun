import sys
from collections import deque

result = []
mans = deque()
num1, num2 = map(int, sys.stdin.readline().strip().split(' '))
mans.extend(range(1, num1+1))
# solution 1
while len(mans) != 0:
    mans.rotate(-num2) # -3이면, [1,2,3,4,5,6,7] -> [4,5,6,7,1,2,3]. 앞에 num2개를 뒤로 보낸다.
    result.append(mans.pop())

# solution 2
while len(mans) != 0:
    for _ in range(num2):
        mans.append(mans.popleft())
    result.append(mans.pop())

print('<'+str(result)[1:-1]+'>')