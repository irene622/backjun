import sys

def parenthesis_string(paren_str):
    stack = []
    for char in paren_str:
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except:
                return 'NO'

    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    commands_num = int(sys.stdin.readline())
    for _ in range(commands_num):
        print(parenthesis_string(sys.stdin.readline().strip()))
