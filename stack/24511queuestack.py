import sys
from collections import deque

# Here are queue, queue = [[1],[4]]. Add 2.
# Then, [[1,2],[4]]->[[2],[4,1]]->[[2],[1]] and return 4
# [[1],[4]] -> [[2],[1],[4]] -> [[2],[1],[4]].pop()
num_data_structure = int(sys.stdin.readline())
data_structure = sys.stdin.readline().strip().split(" ")
data = sys.stdin.readline().strip().split(" ")
queue = deque()
for i in range(num_data_structure):
    if data_structure[i] == "0":
        queue.append(data[i])

num_adding = int(sys.stdin.readline())
adding_elem_list = sys.stdin.readline().strip().split(" ")
for element in adding_elem_list:
    queue.appendleft(element)
    print(queue.pop(), end=" ")
