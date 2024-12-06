import sys

N, C = map(int, sys.stdin.readline().strip().split(" "))
info = {}
seq = sys.stdin.readline().strip().split(" ")
for i, num in enumerate(seq):
    if info.get(num) == None:
        info[num] = 0

    info[num] += 1

sorted_result = sorted(info.items(), key=lambda x: -x[1])

result = ""
for num, freq in sorted_result:
    for _ in range(freq):
        print(num, end=" ")
