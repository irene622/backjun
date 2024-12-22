import sys

sys.stdin = open('data_structure/ex.txt')
N = int(sys.stdin.readline().strip())
numbers = []
for i in range(N):
    numbers += map(int, sys.stdin.readline().strip().split())

print(sorted(numbers, reverse=True)[N-1])


