class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        res_str = "|"

        iterator = self.head
        while iterator is not None:
            res_str += "{}|".format(iterator.data)
            iterator = iterator.next
        return res_str

    def length(self):
        length = 0
        iterator = self.head
        while iterator is not None:
            length += 1
            iterator = iterator.next
        return length

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else: # 링크드리스트에 데이터가 있는경우
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
    def get(self, index):
        iterator = self.head
        for i in range(index):
            iterator = iterator.next
            if iterator == None:
                return None

        return iterator

    def findData(self, data):
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def insert(self, index, data):
        newNode = Node(data)
        indexNode = self.get(index)
        if index >= self.length():
            self.append(data)
        elif index == 0:
            self.prepend(data)
        else:
            newNode.prev = indexNode.prev
            newNode.next = indexNode
            indexNode.prev = newNode

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터 삽입"""
        newNode = Node(data)
        if self.head is None:
            self.append(newNode)
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def delete(self, index):
        # index가 범위 밖이면 에러띄우기
        if index > self.length():
            raise EOFError
        delNode = self.get(index)
        if delNode is self.head:
            self.pop()
        elif delNode is self.tail:
            self.tail = delNode.prev
            self.tail.next = None
        else:
            delNode.prev.next = delNode.next
            delNode.next.prev = delNode.prev
        return delNode.data

    def pop(self):
        if self.length() == 0:
            return
            
        data = self.head.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self._data = data   # 노드가 저장하는 데이터
        self.next = None    # 다음 노드에 대한 레퍼런스
        self.prev = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


linked_list = DoublyLinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
a = linked_list.get(3)

print(a.data)
