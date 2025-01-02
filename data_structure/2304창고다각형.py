import sys

sys.stdin = open('data_structure/ex.txt')
col = int(sys.stdin.readline().strip())
heights = [0 for _ in range(1001)]

max_idx = 0
max_hei = 0
for i in range(col):
    idx, height = map(int, sys.stdin.readline().strip().split(' '))
    heights[idx] = height

    if max_hei <= height:
        max_idx = idx
        max_hei = height

print(max_idx, max_hei)

area = 0
current_height = 0
# 가장 높은것 기준으로, 왼쪽의 넓이
for i in range(max_idx+1):
    higher_height = max(heights[i],current_height)
    area += higher_height
    current_height = higher_height

current_height = 0
for i in range(1000,max_idx,-1):
    higher_height = max(heights[i],current_height)
    area += higher_height
    current_height = higher_height
print('--------')
print(area)