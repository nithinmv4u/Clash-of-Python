list1 = [3,4,2]
list2 = [4,6,5]

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
def save(node,value):
    newnode=ListNode(value)
    newnode.next = node
    return newnode

def concat(ll):
    if(ll.next!=None):
        # print(ll.val)
        return ll.val+concat(ll.next)*10
    else:return ll.val

def addTwoNumbers(l1, l2):
    # print(l1.val)
    num1 = concat(l1)
    num2 = concat(l2)
    print(num1, num2)
    num = num1 + num2
    print(num)
    # list = insert(num*10)
    arr =[]
    list = None
    while(num!=0):
        arr.append(num%10)
        # list = save(list, num % 10)
        num = num // 10
    print(arr)
    for i in range(len(arr)-1,-1,-1):
        list = save(list, arr[i])
    print(list)
    while(list!=None):
        print(list.val)
        list=list.next

if __name__ == '__main__':
    l1 = None
    for i in range(len(list1)):
        l1 = save(l1, list1[i])

    # while(l1!=None):
    #     print(l1.val)
    #     l1=l1.next

    l2 = None
    for i in range(len(list2)):
        l2 = save(l2, list2[i])

    # while(l2!=None):
    #     print(l2.val)
    #     l2=l2.next

    addTwoNumbers(l1,l2)