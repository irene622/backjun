# Stack
commands_num = int(input().strip())
stack = []
for _ in range(commands_num):
    a = input().strip()
    a = [i for i in a.split(' ')]
    
    if a[0] == '1':
        stack.append(a[1])
    elif a[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop()) # 마지막원소 프린트하고, 마지막 원소 제거.
    elif a[0] == '3':
        print(len(stack))
    elif a[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
