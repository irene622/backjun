### copy from https://developerbee.tistory.com/76
import sys


class Heap:
    def __init__(self):
        self.heap = list()
        self.heap.append(None)
        # [None,1,3,5]에서 2가 새로운 숫자. [None,1,3,5,2]이고 현재 idx=4이고 부모 idx는 2.
        # move_up = True이면 바꾼다.
        # [None,1,3,5,2]를 idx를 이용해서 [None,1,2,5,3]으로 바꾼다.


    def pop(self):
        if len(self.heap) <= 1:
            return 0
        else:
            output = self.heap[1]

            # 왜있음?
            self.heap[1] = self.heap[-1]
            del self.heap[-1]

            idx = 1
            while self.move_down(idx):
                left_child_idx = idx*2
                right_child_idx = idx*2+1

                # idx의 오른쪽 자식이 없을 때
                if right_child_idx >= len(self.heap):
                    if self.heap[idx] > self.heap[left_child_idx]:
                        self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                        idx = left_child_idx
                else:
                    # TODO...
                    if self.heap[left_child_idx] < self.heap[right_child_idx]:
                        if self.heap[idx] > self.heap[left_child_idx]:
                            self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                            idx = left_child_idx
                    else:
                        if self.heap[idx] > self.heap[right_child_idx]:
                            self.heap[idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[idx]
                            idx = right_child_idx

            return output


    def move_down(self, idx):
        # Compare current idx and its child idx.
        left_child_idx = idx * 2
        right_child_idx = idx * 2 + 1
        
        # idx의 왼쪽 자식이 없을 때.
        # idx=2의 왼쪽 자식은 idx 4임. 
        # idx 4가 존재하면 len(self.heap)이 5이상임. 아니면 len(self.heap)이 4이하임.
        if left_child_idx >= len(self.heap):
            return False
        
        # idx의 오른쪽 자식이 없을 때.
        # idx 2의 오른쪽 자식은 idx 5임. 
        # idx 5가 존재하면 len(self.heap)이 6이상임. 아니면 len(self.heap)이 5이하임.
        elif right_child_idx >= len(self.heap):
            if self.heap[idx] > self.heap[left_child_idx]:
                return True
            else:
                return False
            
        else:
            # idx 2가 왼쪽자식보다 크면 바꾼다.
            if self.heap[idx] > self.heap[left_child_idx]:
                return True
            # idx 2가 오른쪽자식보다 크면 바꾼다.
            elif self.heap[idx] > self.heap[right_child_idx]:
                return True
            else:
                return False
      

    def move_up(self, idx):
        # Compare current idx and its parents idx.
        if idx <= 1:
            return False
        
        parent_idx = idx // 2
        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False


    def insert(self, num):
        self.heap.append(num)

        idx = len(self.heap) - 1
        while self.move_up(idx):
            parent_idx = idx // 2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx


h = Heap()
sys.stdin = open('data_structure/ex.txt')
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        print(h.pop())
    else:
        h.insert(num)





### copy from https://developerbee.tistory.com/76
# from sys import stdin

# class Heap:
#     def __init__(self):
#         self.heap = list()
#         self.heap.append(None)

#     def move_up(self, idx):
#         if idx <= 1:
#             return False

#         parent_idx = idx // 2
#         if self.heap[idx] < self.heap[parent_idx]:
#             return True
#         else:
#             return False

#     def move_down(self, idx):
#         left_child_idx = idx * 2
#         right_child_idx = idx * 2 + 1

#         # Case1: 왼쪽 자식도 없을 때
#         if left_child_idx >= len(self.heap):
#             return False

#         # Case2: 오른쪽 자식만 없을 때
#         elif right_child_idx >= len(self.heap):
#             if self.heap[idx] > self.heap[left_child_idx]:
#                 return True
#             else:
#                 return False

#         # Case3: 왼쪽, 오른쪽 자식 모두 있을 때
#         else:
#             if self.heap[left_child_idx] < self.heap[right_child_idx]:
#                 if self.heap[idx] > self.heap[left_child_idx]:
#                     return True
#                 else:
#                     return False
#             else:
#                 if self.heap[idx] > self.heap[right_child_idx]:
#                     return True
#                 else:
#                     return False

#     def insert(self, data):
#         self.heap.append(data)

#         idx = len(self.heap) - 1
#         while self.move_up(idx):
#             parent_idx = idx // 2
#             self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
#             idx = parent_idx

#     def pop(self):
#         if len(self.heap) <= 1:
#             print(0)
#         else:
#             print(self.heap[1])

#             self.heap[1] = self.heap[-1]
#             del self.heap[-1]

#             idx = 1
#             while self.move_down(idx):
#                 left_child_idx = idx * 2
#                 right_child_idx = idx * 2 + 1

#                 # Case2: 오른쪽 자식만 없을 때
#                 if right_child_idx >= len(self.heap):
#                     if self.heap[idx] > self.heap[left_child_idx]:
#                         self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
#                         idx = left_child_idx

#                 # Case3: 왼쪽, 오른쪽 자식 모두 있을 때
#                 else:
#                     if self.heap[left_child_idx] < self.heap[right_child_idx]:
#                         if self.heap[idx] > self.heap[left_child_idx]:
#                             self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
#                             idx = left_child_idx
#                     else:
#                         if self.heap[idx] > self.heap[right_child_idx]:
#                             self.heap[idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[idx]
#                             idx = right_child_idx


# h = Heap()
# N = int(stdin.readline())
# for _ in range(N):
#     num = int(stdin.readline())
#     if num == 0:
#         h.pop()
#     else:
#         h.insert(num)