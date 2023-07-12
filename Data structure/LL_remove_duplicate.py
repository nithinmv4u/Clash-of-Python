class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def remove_duplicates(self):
        current = self.head
        unique_list = []
        while current:
            if current.data not in unique_list:
                unique_list.append(current.data)
            current = current.next
        self.head = None
        for i in unique_list[::-1]:
            new_node = Node(i)
            new_node.next = self.head
            self.head = new_node
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(20)
llist.push(11)
llist.push(13)
llist.push(11)
llist.push(13)
llist.push(11)
 
print("Original Linked List: ")
llist.print_list()
 
llist.remove_duplicates()
 
print("\nLinked List after removing duplicates: ")
llist.print_list()
