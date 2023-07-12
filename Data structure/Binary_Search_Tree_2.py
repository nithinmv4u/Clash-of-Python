class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if not curr.left:
                        curr.left = TreeNode(val)
                        break
                    else:
                        curr = curr.left
                elif val > curr.val:
                    if not curr.right:
                        curr.right = TreeNode(val)
                        break
                    else:
                        curr = curr.right
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)
bst.inorder(bst.root) # Output: 1 3 4 5 6 7 8
