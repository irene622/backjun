import sys

sys.stdin = open('data_structure/ex.txt')
info_n, ques_n = map(int, sys.stdin.readline().split())
info = []

for i in range(info_n):
    info.append(sys.stdin.readline().strip())

for i in range(ques_n):
    input = sys.stdin.readline().strip()
    try:
        input = int(input)
        print(info[input-1])
    except:
        print(info.index(input)+1)