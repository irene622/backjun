import sys

game = int(sys.stdin.readline().strip())

alphabet = 'abcdefghijklnmopqrstuvwxyz'
record = {}
count_record = {}
where_record = {}
# for char in alphabet:
#     record[char] = {'count': 0, 'where': []}

for _ in range(game):
    line = sys.stdin.readline().strip()
    count = int(sys.stdin.readline().strip())

    for idx, char in enumerate(line):
        count_record[char] = count_record.get(char, 0) + 1
        where_record[char] = where_record.get(char, []) + [idx]

    cand_lenght = []
    for char, v in count_record.items():
        if v >= count:
            for i in range(0, len(where_record[char])-count+1):
                length = where_record[char][i+count-1] - where_record[char][i]
                cand_lenght.append(length)
    
    # print result
    if len(cand_lenght) == 0:
        print(-1)
    else:
        print(f'{min(cand_lenght)+1} {max(cand_lenght)+1}')

    # initialize
    count_record = {}
    where_record = {}

    
    
