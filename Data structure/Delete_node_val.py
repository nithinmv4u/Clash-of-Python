class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Singlelist:
    def __init__(self):
        self.head = None

    def push(self, value):
        NewNode = Node(value)
        NewNode.next = self.head
        self.head = NewNode

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next

    def delData(self, del_data):
        dataval = self.head
        while dataval.next is not None:
            if(self.head.value == del_data):
                self.head.value = None
                self.head = self.head.next
            if(dataval.next.value == del_data):
                dataval.next.value = None
                if(dataval.next.next == None):
                    dataval.next = None
                    break
                else:
                    dataval.next = dataval.next.next
            dataval = dataval.next

def main():
    data = list(input("Enter values: ").strip().split())
    list1 = Singlelist()
    for i in range(len(data)):
        list1.push(data[i])
    
    list1.listprint()
    del_data = input("Enter the data to be deleted: ").strip().split()[0]
    list1.delData(del_data)
    list1.listprint()

main()