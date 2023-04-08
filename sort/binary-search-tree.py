import tools

# random 값이 20개 들어있는 배열 생성
rand_arr = tools.make_random_arr(20)

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


# 이진트리 만들기
class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = Node(None)

        self.preorder_list=[]
        self.inorder_list=[]
        self.postorder_list=[]

    # 값 추가하기 head가 없을 경우
    def add(self, item):
        if self.head.val is None:
            self.head.val = item

        # head가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__add_node(self.head, item)

    # head가 있는 경우
    def __add_node(self, cur, item):
        print('부모:', cur.val, '자식:', item)
        # head 값이 크면 왼쪽으로
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        # head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    # 찾기!!
    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        print(cur.val, item)
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False



bt = BinaryTree()
for num in rand_arr:
    bt.add(num)

print(bt.search(60))