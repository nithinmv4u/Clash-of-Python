class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Enqueue(node,data):
    NewNode = Node(data)
    if node is not None:
        NewNode.next = node
    return NewNode

def Dequeue(node):
    while node.next is not None:
        prevNode = node
        node = node.next
        Dequeue_data = node.data
    try:
        prevNode.next = None
    except:
        Dequeue_data = node.data
        node.data = None
        prevNode = None
    return Dequeue_data

def printList(node):
    while node is not None:
        print(node.data, end=' ')
        try:
            node = node.next
        except:
            break
    print()

if __name__ == "__main__":
    node = None
    while True:
        print("Select an option: \n1.Enqueue\n2.Dequeue\n3.Exit")
        select = int(input().strip().split()[0])
        if select == 1:
            data = input("Enter Data: ").strip().split()[0]
            node = Enqueue(node, data)
        elif select == 2:
            Dequeue_data = Dequeue(node)
            print("Dequeued: ",Dequeue_data)
            # del(node)
            # node = PrevNode
        elif select == 3:
            break
        else:
            print("Invalid Entry..!")
            continue
        printList(node)