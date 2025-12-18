class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.children = []

def verify_bst(node: Node, min_val: float = float('-inf'), max_val: float = float('inf')):
    if node is None:
        return True
    
    if not (min_val < node.value < max_val):
        return False

    return verify_bst(node.left, min_val, node.value) and verify_bst(node.right, node.value, max_val)


def preorder(root):
    if not root:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]
