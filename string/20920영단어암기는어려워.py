import sys

sys.stdin = open('string/ex.txt', 'r')
N, limit = map(int, sys.stdin.readline().strip().split(' '))

#  'apple' : (count, length, word)
words = {}
for i in range(N):
    word = sys.stdin.readline().strip()
    length = len(word)
    if length >= limit:
        if words.get(word):
            words[word][0] += 1
        else :
            words[word] = [1, length, word]
    else:
        continue

result = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in result:
    print(i[0])

