import sys
from collections import deque

commands_num = int(sys.stdin.readline())
DQ = deque()
for _ in range(commands_num):
    command = sys.stdin.readline().strip()
    if command[:4] == "push":
        DQ.append(int(command.split(" ")[-1]))
    elif command == "pop":
        try:
            print(DQ.popleft())
        except:
            print(-1)
    elif command == "size":
        print(len(DQ))
    elif command == "empty":
        if len(DQ) != 0:
            print(0)
        else:
            print(1)
    elif command == "front":
        try:
            print(DQ[0])
        except:
            print(-1)
    elif command == "back":
        try:
            print(DQ[-1])
        except:
            print(-1)
