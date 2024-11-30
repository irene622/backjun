import sys

N, C = map(int, sys.stdin.readline().strip().split(' '))
info = {}
seq = sys.stdin.readline().strip().split(' ')
for i, num in enumerate(seq):
    if info.get(num) == None:
        info[num] = {'freq': 0, 'order': -1}

    info[num]['freq'] += 1
    if info[num]['order'] == -1:
        info[num]['order'] = i

sorted_result = sorted(info.keys(), key = lambda x: (-info[x]['freq'], info[x]['order'])) 

result = ''
for num in sorted_result:
    result += (num+' ')*info[num]['freq']
print(result.strip())