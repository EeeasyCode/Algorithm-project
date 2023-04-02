import tools

# random 값이 20개 들어있는 배열 생성
rand_arr = tools.make_random_arr(20)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.insert_data(self.root, data)
        return self.root is not None

    def insert_data(self, node, data):
        if node is None:
            node = Node(data)
        
        else:
            if data < node.data:
                node.left = self.insert_data(node.left, data)
            else:
                node.right = self.insert_data(node.right, data)
        
        return node


bst = BST()

for i in rand_arr:
    bst.insert(i)

