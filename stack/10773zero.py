# 10773 제로
import sys

commands_num = int(sys.stdin.readline())
stack = []
for i in range(commands_num):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print('----')
print(sum(stack))