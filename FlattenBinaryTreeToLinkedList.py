class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def flatten(root):
    if not root:
        return
    current = root
    while current:
        if current.left:
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right

            rightmost.right = current.right

            current.right = current.left
            
            current.left = None
        current = current.right
                
def print_linked_list(root):
    while root:
        print(root.val, '->', end=' ')
        root = root.right
    print('null')

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
# Flatten the binary tree to a linked list
flatten(root)
# Print the linked list
print_linked_list(root)
