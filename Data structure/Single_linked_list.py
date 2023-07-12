class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SingleList:
    def __init__(self):
        self.headval = None

    def push(self, value):
        NewNode = Node(value)
        # self.headval = NewNode
        NewNode.nextval = self.headval
        self.headval = NewNode
        print(self.headval )

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval =printval.nextval

list1 = SingleList()
list1.push("Mon")
list1.push("Tue")
list1.push("Wed")
# list1.headval = Node("Mon")
# print(list1.headval.dataval)
# print(list1.headval.nextval)
# e2 = Node("Tue")
# e3 = Node("Wed")
# list1.headval.nextval = e2
# print(list1.headval.nextval)
# e2.nextval = e3

list1.listprint()

