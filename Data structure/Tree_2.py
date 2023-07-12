class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    
    def dfs(self, node):
        if node:
            print(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

# Example usage:
tree = Tree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.dfs(tree.root) # Output: 1 2 4 5 3
