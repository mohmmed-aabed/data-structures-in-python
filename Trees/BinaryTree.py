class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def set_root_value(self, new_obj):
        self.key = new_obj


a = BinaryTree(1)
a.insert_left(2)
a.insert_right(5)

a.left_child.insert_left(3)
a.left_child.insert_right(4)

a.right_child.insert_left(6)
a.right_child.insert_right(7)


preorder_list = []
postorder_list = []
inorder_list = []


def preorder(tree):
    if tree:
        preorder_list.append(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        postorder_list.append(tree.key)


def inorder(tree):
    if tree:
        inorder(tree.left_child)
        inorder_list.append(tree.key)
        inorder(tree.right_child)


preorder(a)
print(preorder_list)
# [1, 2, 3, 4, 5, 6, 7]

postorder(a)
print(postorder_list)
# [3, 4, 2, 6, 7, 5, 1]

inorder(a)
print(inorder_list)
# [3, 2, 4, 1, 6, 5, 7]
