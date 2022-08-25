size = int(input())
#[0,4,2,1,3] = 1번째 퀸은 (0th col, 0th row), 2번째 퀸은 (1th col, 4th row), 3번째 퀸은 (2nd col, 2nd row) ...
#[0,4,2,0,0] #chess의 elements는 맨 위를 0으로 했을 때, 세로의 길이를 의미
#[0,1,2,3,4] #chess의 index는    맨 왼쪽을 0으로 했을때, 가로의 길이를 의미
chess = [0] * size

solution = 0

def check(num_col, my_chess) :
    for i in range(num_col) :
        # 같은 row에 퀸을 놓았니
        if my_chess[num_col] == my_chess[i] :
            return False
        # 대각선에 퀸을 놓았니. 가로의 길이 == 세로의 길이
        if abs(my_chess[num_col] - my_chess[i]) == abs(num_col - i) :
            return False
    return True


def n_queens(num_col, size) :
    global solution
    if num_col == size :
        solution += 1
        return
    else :
        for i in range(size) :
            chess[num_col] = i
            if check(num_col, chess) :
                n_queens(num_col+1, size)

n_queens(0, size)
print(solution)