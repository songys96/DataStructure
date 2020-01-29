from Heap import heapify, heapsort

def swap(tree, parentIndex, childIndex):
    tmp = tree[parentIndex]
    tree[parentIndex] = tree[childIndex]
    tree[childIndex] = tmp


def reverseHeapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산
    if parent_index == 0:
        return
    if tree[parent_index] < tree[index]:
        swap(tree, parent_index, index)
        reverseHeapify(tree, parent_index)

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)
        reverseHeapify(self.heap, len(self.heap)-1)

    def extract_max(self):
        swap(self.heap, 1, len(self.heap)-1)
        maxValue = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        return maxValue

    def __str__(self):
        return str(self.heap)

priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())