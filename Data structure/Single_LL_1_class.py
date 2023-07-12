class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_front(node, value):
    new_node = Node(value)
    new_node.next = node
    return new_node

def print_list(node):
    while node != None:
        print(node.data, end=" ") 
        node = node.next

if __name__ == '__main__':
    list = None
    while True:
        n=int(input("Select an option: \n 1.Add Value \n 2.Exit \n"))
        if n==2:break
        elif n==1:
            value = input("Enter Data: ").strip().split()[0]
            list = add_front(list, value)
            print("Linked List: ", end='')
            print_list(list)
            print()
        else:print("Invalid Input..! Try Again...")





# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = Node()

#     def push(self, value):
#         NewNode = Node(value)
#         # self.headval = NewNode
#         NewNode.nextval = self.headval
#         self.headval = NewNode
#         print(self.headval )

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval =printval.nextval

# list1 = SingleList()
# list1.push("Mon")
# list1.push("Tue")
# list1.push("Wed")
# # list1.headval = Node("Mon")
# # print(list1.headval.dataval)
# # print(list1.headval.nextval)
# # e2 = Node("Tue")
# # e3 = Node("Wed")
# # list1.headval.nextval = e2
# # print(list1.headval.nextval)
# # e2.nextval = e3

# list1.listprint()

# # print(list1.headval.dataval)
# # list1.headval = list1.headval.nextval
# # print(list1.headval.dataval)
# # list1.headval = list1.headval.nextval
# # print(list1.headval.dataval)