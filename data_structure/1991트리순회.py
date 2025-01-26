import sys
from collections import deque

sys.stdin = open('data_structure/ex.txt')
N = int(sys.stdin.readline().strip())

tree = {}
for i in range(N):
    node, left_child, right_child = sys.stdin.readline().strip().split(' ')
    tree[node] = [left_child, right_child]

# preorder traversal
# dfs
def preorder_traversal(bi_tree):
    preorder_path = ''
    stack = ['A']
    visited = {i : False for i in bi_tree.keys()}

    while stack:
        current = stack.pop()
        for i in reversed(bi_tree[current]):   
            if visited[current] is False:
                preorder_path += str(current)
                visited[current] = True
            
            if i == '.':
                continue
            if visited[i] is False:
                stack.append(i)
    return preorder_path

print(preorder_traversal(tree))

##############################
# https://velog.io/@ohk9134/백준-1991번-트리-순회-python-트리-구현
##############################

def inorder(root): # 왼쪽 자식 -> 루트 -> 오른쪽 자식 순으로 탐색
    if root != '.': 
        # 1. root A, inorder(B)
        # 2-1. root B, inorder(D)
        # 3-1. root D, inorder(.)   # 제일 왼쪽 자식을 찾았다!
        # 4. root .     # if root != '.':에 걸리지 않는다.
        # 3-2. 3번으로. print(D, end='')
        # 3-3. root D, inorder(.)
        # 5. root .
        # 2-2. 2번으로. root B. print(B, end='')
        # 2-3. root B, inorder(.)
        # 6. root .
        # 1-2. 1번으로. root A. print(A, end='')
        # 1-3. root A. inorder(C)
        # 7-1. root C, inorder(E)
        # ...
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
inorder('A')

# 3. 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트이므로 재귀함수 순서도 왼쪽 재귀함수 -> 오른쪽 재귀함수 -> root 출력문

def postorder(root): # 왼쪽 자식 -> 오른쪽 자식 -> 루트 순으로 탐색
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root