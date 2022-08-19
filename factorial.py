def factorial(n) :
    if n == 0 :
        return 1
    else :
        n *= factorial(n-1)
        return n


def old_factorial(x) :
    n = 1 # error case : x = 0
    for i in range(1,x+1) :
        n = n * i
    return n


num = int(input())
print(old_factorial(num))