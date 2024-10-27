#STACK
import sys

# (()[[]])은 2*(2 + 3*3)인데, 2*2+2*3*3으로 계산한다.
def value_parente(input):
    answer = 0
    temp = 1
    stack = []
    for i in range(len(input)):
        if input[i] == '(':    
            stack.append(input[i])
            temp *= 2
        
        elif input[i] == '[':
            stack.append(input[i])
            temp *= 3
        
        elif input[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 0
            if input[i-1] == '(':
                # 제일 안쪽의 괄호닫힘이다. temp를 answer에 더해준다.
                answer += temp
            stack.pop()
            temp //= 2

        elif input[i] == ']':
            if len(stack)==0 or stack[-1] != '[':
                return 0
            if input[i-1] == '[':
                # 제일 안쪽의 괄호닫힘이다. temp를 answer에 더해준다.
                answer += temp                
            stack.pop()
            temp //= 3
    
    if len(stack) != 0:
        # 완전히 안 닫힘.
        return 0
    return answer

if __name__ == '__main__':
    input = str(sys.stdin.readline().strip())
    print(value_parente(input))


arr=input()
stack=[]
