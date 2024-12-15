import sys

# max heap
class MaxHeap:
    def __init__(self):
        self.heap = list()
        self.heap.append(None)

    def pop(self):
        if len(self.heap) <= 1:
            output = 0
        else:
            output = self.heap[1]

            self.heap[1] = self.heap[-1]
            del self.heap[-1]

            idx = 1
            while self.move_down(idx):
                child_left_idx = idx * 2
                child_right_idx = idx * 2 + 1

                # 왼쪽 자식만 있는 경우.
                if child_right_idx >= len(self.heap):
                    if self.heap[child_left_idx] > self.heap[idx]:
                        self.heap[child_left_idx], self.heap[idx] = (
                            self.heap[idx],
                            self.heap[child_left_idx],
                        )
                        idx = child_left_idx
                else:
                    # 왼쪽 자식, 오른쪽 자식이 있는 경우.
                    if self.heap[child_left_idx] > self.heap[child_right_idx]:
                        if self.heap[child_left_idx] > self.heap[idx]:
                            self.heap[child_left_idx], self.heap[idx] = (
                                self.heap[idx],
                                self.heap[child_left_idx],
                            )
                            idx = child_left_idx
                    else:
                        if self.heap[child_right_idx] > self.heap[idx]:
                            self.heap[child_right_idx], self.heap[idx] = (
                                self.heap[idx],
                                self.heap[child_right_idx],
                            )
                            idx = child_right_idx

        return output

    def move_down(self, idx):
        child_left_idx = idx * 2
        child_right_idx = idx * 2 + 1

        if child_left_idx >= len(self.heap):
            # 왼쪽 자식 없는 경우.
            # 예, (1, ())이고 heap=[None, 1]. left_idx=2 >= len(heap)=2
            return False
        elif child_right_idx >= len(self.heap):
            # 오른쪽자식 없고, 왼쪽 자식만 있는 경우.
            # 예, (1, (2,))인 상황에서 heap=[None, 1, 2]. right_idx=3 >= len(heap)=3
            if self.heap[child_left_idx] > self.heap[idx]:
                return True
        else:
            if self.heap[child_left_idx] > self.heap[idx]:
                return True
            elif self.heap[child_right_idx] > self.heap[idx]:
                return True
            else:
                return False

    def insert(self, num):
        self.heap.append(num)
        idx = len(self.heap) - 1

        while self.move_up(idx):
            parent_idx = idx // 2
            if self.heap[parent_idx] < self.heap[idx]:
                self.heap[parent_idx], self.heap[idx] = (
                    self.heap[idx],
                    self.heap[parent_idx],
                )
                idx = parent_idx

    def move_up(self, idx):
        if idx <= 1:
            return False

        parent_idx = idx // 2
        if self.heap[parent_idx] < self.heap[idx]:
            return True
        else:
            return False


sys.stdin = open("data_structure/ex.txt")
N = int(sys.stdin.readline())
heap = MaxHeap()
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        print(heap.pop())
    else:
        heap.insert(num)



############ 파이썬 heapq 이용
import heapq
N = int(sys.stdin.readline().strip())

max_heap = []

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    
    if n == 0:
        if len(max_heap):
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -n)