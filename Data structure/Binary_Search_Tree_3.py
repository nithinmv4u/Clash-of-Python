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
    
    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(8)
bst.preorder(bst.root)
