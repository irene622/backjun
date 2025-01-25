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

