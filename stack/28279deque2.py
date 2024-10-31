import sys
from collections import deque

commands_num = int(sys.stdin.readline())
my_deque = deque()
for _ in range(commands_num):
    command = sys.stdin.readline().strip()
    if command[0] == '1':
        my_deque.appendleft(command.split(' ')[-1])
    elif command[0] == '2':
        my_deque.append(command.split(' ')[-1])
    elif command == '3':
        try:
            print(my_deque.popleft())
        except:
            print(-1)
    elif command == '4':
        try:
            print(my_deque.pop())
        except:
            print(-1)
    elif command == '5':
        print(len(my_deque))
    elif command == '6':
        if len(my_deque)== 0 :
            print(1)
        else:
            print(0)
    elif command == '7':
        try:
            print(my_deque[0])
        except:
            print(-1)
    elif command == '8':
        try:
            print(my_deque[-1])
        except:
            print(-1)