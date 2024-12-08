import sys

# max heap
class MaxHeap():
    def __init__(self):
        self.heap = list()
        self.heap.append(None)

    def pop(self):
        if len(heap) <= 1:
            output = 0
        else:
            output = self.heap.pop(1)

            self.heap[1] = self.heap[-1]
            del self.heap[-1]

            


sys.stdin = open("data_structure/ex.txt")
N = int(sys.stdin.readline())
heap = MaxHeap()
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        print(heap.pop())
    else:
        heap.insert(num)

