class Node:
    def __init__(self, data):
      self.left = None
      self.data = data
      self.right = None

    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.data is not None:
            if self.left:
                self.left.printTree()
            print(self.data)
            if self.right:
                self.right.printTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

if __name__ == '__main__':
    root = None
    while True:
        print("Select an Option: \n1.Add Value\n2.Exit")
        n=int(input().strip().split()[0])
        if n==1:
            data = int(input("Enter Number: ").strip().split()[0])
            if root is None:
                root = Node(data)
            else:
                root.insert(data)
        else:
            break
        root.printTree()
    print(root.inorderTraversal(root)) 