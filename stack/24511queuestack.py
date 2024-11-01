import sys
from collections import deque

num_data_structure = int(sys.stdin.readline())
data_structure = sys.stdin.readline().strip().split(' ')
data_list = []
for element in sys.stdin.readline().strip().split(' '):
    one_deque = deque()
    one_deque.append(element)
    data_list.append(one_deque)

num_adding = int(sys.stdin.readline())
adding_elem_list = sys.stdin.readline().strip().split(' ')
result = ''
for adding in adding_elem_list:
    for i in range(num_data_structure):
        if data_structure[i] == '0': # queue
            data_list[i].append(adding)
            adding = data_list[i].popleft()
        elif data_structure[i] == '1': # stack
            data_list[i].append(adding)
            adding = data_list[i].pop()
    result += adding + ' '
print(result.strip())
