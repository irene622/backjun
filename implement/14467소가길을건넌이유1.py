import sys

sys.stdin = open('implement/ex.txt')
N = int(sys.stdin.readline().strip())
info = {}
total_change = 0
for _ in range(N):
    cow, road = map(int, sys.stdin.readline().strip().split(' '))

    if info.get(cow) == None:
        info[cow] = road
    else:
        amount_of_change = abs(info[cow] - road)
        info[cow] = road
        total_change += amount_of_change

print(info)
print(total_change)
