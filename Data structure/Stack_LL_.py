class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(node, value):
    new_node = Node(value)
    new_node.next = node
    return new_node

def pop(node):
    if node is not None:
        updated_node = node.next
        print("Popped data:", node.data)
        del(node)
        return updated_node
    else:
        print("No More data in stack..!")
        return None

def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

if __name__ == '__main__':
    list = None
    # size = 
    while True:
        if list is not None:
            n=int(input("Select an option: \n 1.Push \n 2.Pop \n 3.Exit \n"))
        else:
            n=int(input("Select an option: \n 1.Push \n 3.Exit \n"))
        if n==1:
            value = input("Enter Data: ").strip().split()[0]
            list = push(list, value)
        elif n==2:
            if list is not None:
                list = pop(list)
            else:
                print("Invalid Input..! Try Again...")
                continue
        elif n==3:break
        else:print("Invalid Input..! Try Again...")
        print("Linked List: ", end='')
        print_list(list)
        print()