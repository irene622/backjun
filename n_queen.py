size = int(input())

chess = [0] * size
solution = 0

def check(num_col, chess) :
    for i in range(num_col) :
        if chess[num_col] == chess[i] :
            return False
        if abs(chess[num_col] - chess[i]) == abs(num_col - i) :
            return False

    return True


def n_queen(num_col, size) :
    global solution
    if num_col == size :
        solution += 1
        return
    else :
        for i in range(size) :
            chess[num_col] = i
            if check(num_col, chess) :
                n_queen(num_col+1, size)

n_queen(0, size)
print(solution)