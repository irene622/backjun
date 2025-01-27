import sys

sys.stdin = open('data_structure/ex.txt')
N = int(sys.stdin.readline().strip())

abs_sort = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        abs_sort.append(num)
    elif num == 0:
        abs_sort.pop()