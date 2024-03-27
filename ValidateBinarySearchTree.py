class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def validate_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not min_val <= root.data <= max_val:
        return False
    left_search = validate_bst(root.left, min_val, root.data)
    right_search = validate_bst(root.right, root.data, max_val)
    return left_search and right_search

# Input handling
t = int(input())
for _ in range(t):
    elements = list(map(int, input().split()))
    n = len(elements)
    tree = [BinaryTreeNode(elements[i]) if elements[i] != -1 else None for i in range(n)]
    i, j = 0, 1
    while i < n:
        if tree[i] is not None:
            tree[i].left = tree[j]
            j += 1
            tree[i].right = tree[j]
            j += 1
        i += 1

# Check if the tree is a valid BST
print(validate_bst(tree[0]))
