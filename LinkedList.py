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

        return iterator

    def findData(self, data):
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
linked_list.append(5)
linked_list.append(3)
linked_list.append(2)

print(linked_list)
linked_list.prepend(310)
print(linked_list)