# Binary Tree Traversals:
    # Preorder: visit root node, traverse TL, traverse TR
    # Inorder: traverse TL, visit root node, traverse TR
    # Postorder: traverse TL, traverse TR, visit root node.
    # Examlpe:
#                    a
#                b       c
#             d    e    f
#              g  h    i  j
#   Preorder sequence: a, b, d, g, e, h, c, f, i, j
#   Inorder: d, g, b, h, e, a, i, f, j, c
#   Postorder: g, d, h, e, b, i, j, f, c, a


class Node:


    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:


    def __init__(self):

        self.root = None


    def search(self, desired_key):

        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
                
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
                
            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right
    
        # The key was not found in the tree.
        return None
    

    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None: 
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
        

    def remove(self, key):

        parent = None
        current_node = self.root
        
        # Search for the node.
        while current_node is not None:
        
            # Check if current_node has a matching key.
            if current_node.key == key: 
                if current_node.left is None and current_node.right is None:   # Case 1
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node: 
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed
                elif current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node: 
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed
                else:                                    # Case 3
                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.key = successor.key      # Copy successor to current node
                    parent = current_node
                    current_node = current_node.right     # Remove successor from right subtree
                    key = parent.key                      # Loop continues with new key
            elif current_node.key < key: # Search right
                parent = current_node
                current_node = current_node.right
            else:                        # Search left
                parent = current_node
                current_node = current_node.left
                
        return # Node not found


# Check if a binary tree is BST or not

INT_MAX = 4294967296
INT_MIN = -4294967296


def isBST(node):
    
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 

def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.key < mini or node.key > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.key -1) and
          isBSTUtil(node.right, node.key+1, maxi))


# Tree Traversals

def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.key),
 
        # now recur on right child
        printInorder(root.right)
 

def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.key),
 

def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.key),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
root = Node(79)
root.left = Node(66)
root.right = Node(88)
root.left.left = Node(50)
root.left.right = Node(78)
root.left.right.left = Node(77)
root.right.left = Node(86)
root.right.left.left = Node(82)
root.right.left.left.right = Node(83)
root.right.right = Node(90)
root.right.right.left = Node(89)
root.right.right.right = Node(94)