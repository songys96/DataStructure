class LinkedList:
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
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
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
        prevNode = self.get(index-1)
        if prevNode is self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            newNode.next = prevNode.next
            prevNode.next = newNode

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터 삽입"""
        newNode = Node(data)
        if self.head == None:
            self.append(newNode)
        else:
            newNode.next = self.head
            self.head = newNode

    def delete(self, index):
        # index가 범위 밖이면 에러띄우기
        if index > self.length():
            raise EOFError
        delNode = self.get(index)
        if delNode is self.head:
            self.pop()
        elif delNode is self.tail:
            prevNode = self.get(index - 1)
            prevNode.next = None
            self.tail = prevNode
        else:
            prevNode = self.get(index - 1)
            prevNode.next = delNode.next
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
        return data

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self._data = data   # 노드가 저장하는 데이터
        self.next = None    # 다음 노드에 대한 레퍼런스

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.append(11)
linked_list.append(7)

print(linked_list)
linked_list.pop()
print(linked_list)