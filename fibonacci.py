def fibonacci(n) :
    if n == 0 :
        return 0
    elif n== 1 :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def old_fibonacci(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    fibo_n_1 = 1
    fibo_n_2 = 0
    # iteration = 2
    for i in range(n-1) :
        fibo = fibo_n_1 + fibo_n_2
        # if iteration == n :
            # return fibo
        # iteration += 1
        fibo_n_2 = fibo_n_1
        fibo_n_1 = fibo
    return fibo

num = int(input())
print(fibonacci(num))
print(old_fibonacci(num))