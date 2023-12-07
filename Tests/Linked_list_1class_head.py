class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def save(self, listOne):
        head = ListNode(None)
        newNode = head
        for i in range(len(listOne)):
            newNode.next = ListNode(listOne[i])
            newNode = newNode.next
        return head.next

def display(node):
    while(node != None):
        print(node.val)
        node = node.next

listOne = [1,2,4]
listTwo = [1,3,4]
list1 = Solution().save(listOne)

# list2 = None
# for i in range(len(listTwo)-1,-1,-1):
#     list2 = save(list2, listTwo[i])

display(list1)
# display(list2)