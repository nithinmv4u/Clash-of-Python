class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None

    def push(self, value):
        NewNode = Node(value)
        NewNode.next = self.head
        self.head =NewNode

    def at_end(self, value):
        travel = self.head
        while travel.next is not None:
            travel = travel.next
        travel.next = Node(value)

    def printval(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next

def main():
    slist = SingleList()
    slist.push("Mon")
    slist.push("Tue")
    slist.push("Wed")
    slist.printval()
    beg_val = input("Enter a value to add at begining: ").strip().split()[0] #insert value at begining
    slist.push(beg_val)
    slist.printval()
    end_val = input("Enter a value to add at end: ").strip().split()[0]
    slist.at_end(end_val)
    slist.printval()

main()