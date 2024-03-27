class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def zigzag(root):
    if not root:
        return
    current_level = []
    next_level = []
    left_to_right = True
    current_level.append(root)
    while current_level:
        node = current_level.pop()
        print(node.data, end = ' ')
        if left_to_right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        if not current_level:
            left_to_right = not left_to_right
            current_level, next_level = next_level, current_level

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    zigzag(root)
    