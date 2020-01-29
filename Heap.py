"""
힙
완전이진트리 -> 마지막 계층이 좌측부터 순서대로
힙 속성 -> 모든 노드들은 자식노드보다 커야한다
[None, 1, 2, 3, 4, 5, 6, 7] 
맨 앞의 None은 인덱스의 편함을 위한 것이자 루트노드의 부모노드는 None을 의미
"""
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]

def swap(tree, parentIndex, childIndex):
    tmp = tree[parentIndex]
    tree[parentIndex] = tree[childIndex]
    tree[childIndex] = tmp

def heapify(tree, nodeIndex, treeSize):

    leftChildIndex = nodeIndex * 2
    rightChildIndex = nodeIndex * 2 + 1

    if treeSize-1 >= leftChildIndex:
        if tree[nodeIndex] < tree[leftChildIndex]:
            swap(tree, nodeIndex, leftChildIndex)
            heapify(tree, leftChildIndex, treeSize)
    if treeSize-1 >= rightChildIndex:
        if tree[nodeIndex] < tree[rightChildIndex]:
            swap(tree, nodeIndex, rightChildIndex)
            heapify(tree, rightChildIndex, treeSize)

def heapsort(tree):
    treeSize = len(tree)
    for i in range(treeSize, 0, -1):
        heapify(tree, i, treeSize)
    for j in range(treeSize-1, 0, -1):
        swap(tree, 1, j)
        heapify(tree, 1, j)

data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)