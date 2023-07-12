class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_LL:
    def __init__(self):
        self.head = None

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def reverseprint(self):
        printval = self.head
        while printval.next is not None:
            printval = printval.next
        while printval is not None:
            print(printval.data)
            printval = printval.prev
        

dllist = Double_LL()
dllist.push("mon")
dllist.push("tue")
dllist.push("wed")
dllist.listprint()
dllist.reverseprint()