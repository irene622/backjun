import sys

game = int(sys.stdin.readline().strip())

alphabet = 'abcdefghijklnmopqrstuvwxyz'
record = {}
for char in alphabet:
    record[char] = {'count': 0, 'where': []}

for _ in range(game):
    line = sys.stdin.readline().strip()
    count = int(sys.stdin.readline().strip())

    for idx, char in enumerate(line):
        record[char]['count'] += 1
        record[char]['where'].append(idx)

    cand_lenght = []
    for char, info in record.items():
        if info['count'] >= count:
            for i in range(0, len(info['where'])-count+1):
                length = record[char]['where'][i+count-1] - record[char]['where'][i]
                cand_lenght.append(length)
    
    # print result
    if len(cand_lenght) == 0:
        print(-1)
    else:
        print(f'{min(cand_lenght)+1} {max(cand_lenght)+1}')

    # initialize
    record = {}
    for char in alphabet:
        record[char] = {'count': 0, 'where': []}

    
    
