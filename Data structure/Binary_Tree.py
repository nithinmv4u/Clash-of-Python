class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        print("self.data: ",self.data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    print("Left Insert: ",data)
                    self.left = Node(data)
                else:
                    print("Go Left")
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    print("Right Insert: ",data)
                    self.right = Node(data)
                else:
                    print("Go Right")
                    self.right.insert(data)
        else:
            print("Insert: ",data)
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data, end=' '),
        if self.right:
            # print("right")
            self.right.PrintTree()

if __name__ == '__main__':
    root = None
    while True:
        n=int(input("Select an option: \n 1.Add Value \n 2.Exit \n"))
        if n==2:break
        elif n==1:
            value = int(input("Enter Data: ").strip().split()[0])
            if root is None:
                print("Insert: ",value)
                root = Node(value)
            else:
                root.insert(value)
            # list = add_front(list, value)
            # print("Linked List: ", end='')
            root.PrintTree()
            print()
        else:print("Invalid Input..! Try Again...")
# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()