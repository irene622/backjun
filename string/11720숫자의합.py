import sys

N = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip()
sum = 0
for i in range(N):
    sum += int(numbers[i])
print(sum)