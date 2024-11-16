import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
sys.stdin = open('string/9406.txt', 'r')
N = int(sys.stdin.readline().strip())

for i in range(N):
    line = sys.stdin.readline().strip()
    count = {i:0 for i in alphabet}
    for char in line:
        if char == ' ':
            continue
        count[char] += 1

    num_max = max(count.values())
    _result = []
    for k,v in count.items():
        if num_max == v:
            _result.append(k)

    if len(_result) == 1:
        print(_result[0])
    else:
        print('?')

