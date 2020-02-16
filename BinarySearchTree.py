class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def printSortedTree(self):
        def print_inorder(node):
            if node is not None:
                print_inorder(node.left_child)
                print(node.data)
                print_inorder(node.right_child)
        print_inorder(self.root)
        
    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        if self.root is None:
            return None

        temp = self.root
        while temp is not None:
            if temp.data == data:
                return temp
            if temp.data < data:
                temp = temp.right_child
            else:
                temp = temp.left_child
        return None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while temp is not None:
            if data > temp.data:
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                else:
                    temp = temp.right_child
            else:
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                else:
                    temp = temp.left_child

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때 
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else:
                if node_to_delete is parent_node.right_child:
                    parent_node.right_child = None
                else:
                    parent_node.left_child = None
        
        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때
        # 오른쪽 자식만 있을경우
        elif node_to_delete.left_child is None: 
            # 지우려는 노드가 루트노드일경우
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽일경우
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽일경우s
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            
        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parnet = None
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        else:
            succesor = BinarySearchTree.find_min(node_to_delete.right_child)
            node_to_delete.data = succesor.data
            # 기준값 바로 아래 있을경우
            if succesor.parent.right_child is succesor:
                succesor.parent.right_child = succesor.right_child
            # 기본적인 값
            else:
                succesor.parent.left_child = succesor.right_child
            if succesor.right_child is not None:
                succesor.right_child.parent = succesor.parent
                



    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp = node
        while temp.left_child is not None:
            temp = temp.left_child

        return temp

# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.printSortedTree()