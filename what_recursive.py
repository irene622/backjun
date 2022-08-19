bar_num = 0
a = '"재귀함수가 뭔가요?"'
b1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
b2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
b3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
c = '"재귀함수는 자기 자신을 호출하는 함수라네"'
d = '라고 답변하였지.'

def recursive_is(n) :
    global bar_num
    if n == 0 :
        print('____'*bar_num + a)
        print('____'*bar_num + c)
        print('____'*bar_num + d)
        return
    else :
        print('____'*bar_num + a)
        print('____'*bar_num + b1)
        print('____'*bar_num + b2)
        print('____'*bar_num + b3)
        bar_num += 1
        recursive_is(n-1)
        bar_num -= 1
        print('____'*bar_num + d)


num = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursive_is(num)