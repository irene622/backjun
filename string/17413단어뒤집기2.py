import sys

line = sys.stdin.readline().strip()

# Using stack
stack = []
ans = ''
open = False
for char in line:
    if char == '<':
        open = True
        for i in range(len(stack)):
            ans += stack.pop()
    
    stack.append(char)
    if char == '>':
        open = False
        for _ in range(len(stack)):
            ans += stack.pop(0)
        
    if open == False:
        if char == ' ':
            for i in range(len(stack)):
                if i == 0:
                    stack.pop()
                    continue
                ans += stack.pop()
            ans += ' '

if len(stack) != 0:
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)
