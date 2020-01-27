"""
Hash Table

고정된 크기의 배열을 만든다
해시함수를 이용해서 key를 원하는 범위의 자연수로 만든다
해시 함수 결과값 인덱스에 key-value를 저장한다
<조건>
한 해시 테이블의 해시함수는 결정론적이어야 한다 -> 같은 값을 넣으면 항상 같은 결과
결과 해시값이 치우치지 않고 고르게 나와야 한다.
빨리 계산할 수 있어야한다.
"""

def hashFunction(key, arraySize, a):
    # a는 0~1사이의 임의의 고정값
    a = 0.6666
    temp = a * key
    temp = temp - int(temp)
    return int(arraySize * temp)

"""
충돌 처리 방법 
Chaining - LinkedList 이용
탐색(find), 삽입(append), 삭제(delete)
"""
# HashTable 구현
from HashTableLinkedList import Node, LinkedList
class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]

    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)
        return res_str[:-1]

    def _hashFunction(self, key):
    # a는 0~1사이의 임의의 고정값
        return hash(key) % self._capacity

    def _getLinkedList(self, key):
        hash_id = self._hashFunction(key)
        return self._table[hash_id]

    def _lookUpNode(self, key):
        linkedList = self._getLinkedList(key)
        node = linkedList.find_node_with_key(key)
        return node

    def _lookUpValue(self, key):
        return self._lookUpNode(key).value

    def insert(self, key, value):
        existingNode = self._lookUpNode(key)
        if existingNode is not None:
            existingNode.value = value
        else:
            LinkedList = self._getLinkedList(key)
            LinkedList.append(key, value)

    def delete(self, key):
        existingNode = self._lookUpNode(key)
        if existingNode is not None:
            LinkedList = self._getLinkedList(key)
            LinkedList.delete(existingNode)


test_scores = HashTable(50) # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores._lookUpValue("현승"))
print(test_scores._lookUpValue("태호"))
print(test_scores._lookUpValue("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)

























# LinkedList and Node Def 

