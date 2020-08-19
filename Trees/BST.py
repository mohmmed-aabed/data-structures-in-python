class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print(data, 'is already present in the tree!')

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

    def get_size(self):
        if self.root:
            return self._get_size(self.root)
        else:
            return 0

    def _get_size(self, cur_node):
        if cur_node.left and cur_node.right:
            return 1 + self._get_size(cur_node.left) + self._get_size(cur_node.right)
        elif cur_node.left:
            return 1 + self._get_size(cur_node.left)
        elif cur_node.right:
            return 1 + self._get_size(cur_node.right)
        else:
            return 1

    def get_height(self):
        if self.root:
            return self._get_height(self.root)
        else:
            return 0

    def _get_height(self, cur_node):
        if cur_node.left and cur_node.right:
            return 1 + max(self._get_height(cur_node.left), self._get_height(cur_node.right))
        elif cur_node.left:
            return 1 + self._get_height(cur_node.left)
        elif cur_node.right:
            return 1 + self._get_height(cur_node.right)
        else:
            return 1

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)

    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(cur_node.data)
            self._inorder_print(cur_node.right)

    def is_bst(self):
        if self.root:
            is_satisfied = self._is_bst(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst(cur_node.right, cur_node.right.data)
            else:
                return False

    def get_min(self):
        if self.root:
            return self._get_min(self.root)
        else:
            return None

    def _get_min(self, cur_node):
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node.data

    def get_max(self):
        if self.root:
            return self._get_max(self.root)
        else:
            return None

    def _get_max(self, cur_node):
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node.data


# Binary Search Tree
bst = BST()
for num in [10, 4, 16, 1, 7, 13, 19]:
    bst.insert(num)

print(bst.find(13))
# True
print(bst.find(15))
# False

print('Size =', bst.get_size())
# Size = 7
print('Height =', bst.get_height())
# Height = 3

bst.inorder_print()
# 1
# 4
# 7
# 10
# 13
# 16
# 19

print(bst.is_bst())
# True

print(bst.get_min())
# 1

print(bst.get_max())
# 19


# Normal Tree
tree = BST()
# The First Level
tree.root = Node(1)
# The Second Level
tree.root.left = Node(2)
tree.root.right = Node(3)
# The Third Level
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print('Size =', tree.get_size())
# Size = 7
print('Height =', tree.get_height())
# Height = 3

tree.inorder_print()
# 4
# 2
# 5
# 1
# 6
# 3
# 7

print(tree.is_bst())
# False
