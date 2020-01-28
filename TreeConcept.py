"""
트리
부모노드는 자식노드들을 가르키는 레퍼런스를 가지고 있음

                    rootNode                        - 깊이 0
            Node                Node                - 깊이 1
형제노드 Node    Node    leafNode   parentNode       - 깊이 2
                                childNode childNode - 깊이 3

트리를 쓰면 다양한 문제들을 기발하게 해결
1. 정렬문제     2. 압축문제
3. 다양한 추상 자료형 구현!!              
"""

"""
이진트리 
 - 각 노드가 최대 2개만 가진다
"""

class Node:
    """ 이진 트리 노드 클래스"""
    def __init__(self, data):
        """데이터아 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_node = None
        self.right_node = None


"""
전 이진 트리 
Full Binary Tree
모든 노드가 0개 혹은 2개의 자식을 갖는 이진 트리
"""

"""
완전 이진 트리
Complete Binary Tree
마지막 레벨 직전의 레벨까지 모든 노드들이 다 채워졌을때
단, 마지막 레벨은 왼쪽에서 오른쪽으로 차야함

리스트 = [1,2,3,4,5,6,7,8,9] 이 순서대로 있을때
                1
        2              3
    4       5       6       7
  8   9      

가장 왼쪽이 2의 제곱수로 증가함을 통해 빠른 인덱싱 가능!
2를 곱하거나 나눠서 찾기!!
왼쪽 자식노드면 부모노드의 *2
오른쪽 자식노드면 부모노드의 *2+1
부모노드는 자식노드의 /2의 몫

6번째 노드의 부모노드는 6/2



"""

"""
포화 이진 트리
perfect Binary Tree
완전히 다 채워져 있는 이진트리
"""