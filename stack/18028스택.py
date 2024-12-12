import sys
from collections import deque

sys.stdin = open("stack/ex.txt", "r")
num_lines = int(sys.stdin.readline().strip())

my_deque = deque()
for _ in range(num_lines):
    line = sys.stdin.readline().strip()

    if "push" in line:
        a, b = line.split(" ")
        my_deque.append(int(b))
    elif "pop" == line:
        if len(my_deque) != 0:
            print(my_deque.pop())
        else:
            print(-1)
    elif "size" == line:
        print(len(my_deque))
    elif "empty" == line:
        if len(my_deque) != 0:
            print(0)
        else:
            print(1)
    elif "top" == line:
        if len(my_deque) != 0:
            print(my_deque[-1])
        else:
            print(-1)
