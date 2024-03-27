class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def tree_paths_sum_util(self, node, val):
        if not node:
            return 0
        val = val*10 + node.data
        if not node.left and not node.right:
            return val
        return (self.tree_paths_sum_util(node.left, val) + self.tree_paths_sum_util(node.right, val))
    
    def tree_paths_sum(self, node):
        return self.tree_paths_sum_util(node, 0)
    
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(3)
    tree.root.right = Node(5)
    tree.root.right.right = Node(4)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(5)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)
    print(tree.tree_paths_sum(tree.root))