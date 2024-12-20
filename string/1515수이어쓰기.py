import sys

number_origin = sys.stdin.readline().strip()

# 12345678910 -> 2340 -> output = 10
idx = 0
while True:
    # '1' == number_origin[0] -> False.
    # '2' == number_origin[0] -> True. '3' == number_origin[1] -> True. '4' == number_origin[2] -> True. ...
    # n = 10. '0' == number_origin[3] -> True. idx += 1 -> idx = 4 -> idx == len(number_origin) -> True.
    for n in range(1, 3001):
        for char in str(n):
            if number_origin[idx] == char:
                idx += 1
            if idx == len(number_origin):
                print(n)
                exit()

idx = 0
n = 1
while True:
    for char in str(n):
        if number_origin[idx] == char:
            idx += 1
        if idx == len(number_origin):
            print(n)
            exit()
    n += 1
