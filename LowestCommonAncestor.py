class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
def build_tree(arr):
    if not arr or arr[0] == "N":
        return None
    root = Node(int(arr[0]))
    queue = [root]
    i = 1
    while queue and i < len(arr):
        curr_node = queue.pop(0)
        curr_val = arr[i]
        if curr_val != "-1":
            curr_node.left = Node(int(curr_val))
            queue.append(curr_node.left)
        i += 1
        if i >= len(arr):
            break
        curr_val = arr[i]
        if curr_val != "-1":
            curr_node.right = Node(int(curr_val))
            queue.append(curr_node.right)
        i += 1
    return root

def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    if left_lca is not None and right_lca is not None:
        return root
    return left_lca if left_lca is not None else right_lca

# Input
s = input().split()
root = build_tree(s)
x, y = map(int, input().split())
# Find LCA
ans = find_lca(root, x, y)
print(ans.data if ans else "N")
