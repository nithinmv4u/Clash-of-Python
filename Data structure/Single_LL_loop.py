#Not Working

class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SingleList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

def main():
    node = int(input("Enter number of nodes: "))
    list1 = SingleList()
    head = list1.headval
    for i in range(node):
        data =input("Enter data: ")
        head = Node(data)
        head.nextval = head
        # print(head.dataval)
        # print(head.nextval)
    # print(list1)
    list1.listprint()

main()