class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None  # By default it is NONE
        self.right = None  # By default it is NONE


class BianryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_tree(self, transversal_type):
        if transversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif transversal_type == "inorder":
            return self.inorder_print(self.root, "")
        else:
            print(f"Traversal type {transversal_type} is not supported")
            return False

    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        # if star is not Null
        if start:
            # star.value is the value of "Node":star
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal


#         1
#        / \
#       2   3
#      /\   /\
#     4  5  6 7
#              \
#               8


# Setup Binary Tree
tree = BianryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


# Trevarsal of Binar Tree

# Preorder: 1-2-4-5-3-6-7-8-
print(tree.print_tree("preorder"))

# Inorder: 4-2-5-1-6-3-7-8-
print(tree.print_tree("inorder"))
