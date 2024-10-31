import sys

while True:
    sentence = sys.stdin.readline()
    if sentence == '.\n':
        break

    stack = []
    result = None
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
            # if - else말고 다른 대안. len(stack)==0인것 때문에 try - excetp를 두개썼다.
            # try:
            #     if stack[-1] == '(':
            #         stack.pop()
            #     else:
            #         result = 'no'
            # except:
            #     result = 'no'
        elif char == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
            # try:
            #     if stack[-1] == '[':
            #         stack.pop()
            #     else:
            #         result = 'no'
            # except:
            #     result = 'no'
    if result == None:
        if len(stack) == 0 :
            result = 'yes'
        else:
            result = 'no'
    print(result)