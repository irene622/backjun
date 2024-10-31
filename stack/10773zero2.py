# 10773 제로
import sys

commands_num = int(sys.stdin.readline())
prev_num = 0
result = 0
for i in range(commands_num):
    num = int(sys.stdin.readline())
    if num == 0:
        result -= prev_num
    else:
        result += num
    prev_num = num
print('----')
print(result)
# 0이 두번이상 나올 상황을 예상못함.