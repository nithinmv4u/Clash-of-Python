class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self):
      self.head = None

    def push(self, value):
        NewNode = Node(value)
        NewNode.next = self.head
        self.head = NewNode

    def printval(self):
        printvalu = self.head
        while printvalu is not None:
            print(printvalu.data)
            printvalu = printvalu.next

def main():
    arr = list(map(int,input("Enter values: ").strip().split()))
    list1 = SingleList()
    for i in range(len(arr)):
        list1.push(arr[i])

    list1.printval()

main()