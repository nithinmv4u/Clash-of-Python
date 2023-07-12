class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_before_after(self, x, data_before, data_after):
        new_node_before = Node(data_before)
        new_node_after = Node(data_after)
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                new_node_before.next = current_node
                new_node_after.next = current_node.next
                current_node.next = new_node_after
                if current_node == self.head:
                    self.head = new_node_before
                else:
                    prev_node.next = new_node_before
                break
            prev_node = current_node
            current_node = current_node.next
        else:
            print(f"Node with data {x} not found in the linked list")

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

def main():
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)

    linked_list.head.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node

    linked_list.print_list()  # Output: 1 2 3 4

    linked_list.insert_before_after(1, 5, 6)

    linked_list.print_list()  # Output: 1 2 5 3 6 4

main()



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Singlelist:
#     def __init__(self):
#         self.head = None

#     def push(self, value):
#         NewNode = Node(value)
#         NewNode.next = self.head
#         self.head = NewNode

#     def listprint(self):
#         printval = self.head
#         while printval is not None:
#             print(printval.value)
#             printval = printval.next

#     def insertData(self, x_data):
#         dataval = self.head
#         while dataval.next is not None:
#             print("val: ",dataval.value)
#             if(self.head.value == x_data):
#                 print("first")
#                 PrevNode = Node("prev")
#                 PrevNode.next = self.head
#                 self.head = PrevNode
#                 NextNode = Node("next")
#                 NextNode.next = dataval.next
#                 dataval.next = NextNode
#             if(dataval.next.value == x_data):
#                 print(dataval.next.value)
#                 PrevNode = Node("prev")
#                 PrevNode.next = dataval.next
#                 print(PrevNode.next.value)
#                 dataval.next = PrevNode
#                 print(dataval.next.value)
#                 NextNode = Node("next")
#                 NextNode.next = PrevNode.next.next
#                 PrevNode.next.next = NextNode
#                 if(dataval.next.next == None):
#                     dataval.next = None
#                     break
#                 else:
#                     dataval.next = dataval.next.next
#             dataval = dataval.next

# def main():
#     data = list(input("Enter values: ").strip().split())
#     list1 = Singlelist()
#     for i in range(len(data)):
#         list1.push(data[i])
    
#     list1.listprint()
#     x_data = input("Enter the data: ").strip().split()[0]
#     list1.insertData(x_data)
#     list1.listprint()

# main()