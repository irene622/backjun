import sys

sys.stdin = open('data_structure/ex.txt')
col = int(sys.stdin.readline().strip())
info = []
for i in range(col):
    idx, hei = map(int, sys.stdin.readline().strip().split(' '))
    info.append((idx, hei))

info = sorted(info, key=lambda x : x[0])
print(info)