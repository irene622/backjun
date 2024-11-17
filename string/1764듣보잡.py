import sys

sys.stdin = open('string/1764.txt', 'r')
no_heard, no_look = map(int, sys.stdin.readline().strip().split(' '))

no_heard_set = set()
for i in range(no_heard):
    no_heard_set.add(sys.stdin.readline().strip())

no_looking_set = set()
for i in range(no_look):
    no_looking_set.add(sys.stdin.readline().strip())

result = sorted(no_heard_set & no_looking_set)
print(len(result))
for i in result:
    print(i)
