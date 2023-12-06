# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def save(node, val):
    newNode = ListNode(val)
    newNode.next = node
    return newNode

def display(node):
    while(node != None):
        print(node.val)
        node = node.next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        mergedList = None
        while(list1 != None):
            while(list2 != None):
                if list1.val < list2.val:
                    mergedList = ListNode(list1.val)
                    # mergedList.val = list1.val
                    mergedList = mergedList.next
                    list1 = list1.next
                else:
                    mergedList = ListNode(list2.val)
                    # mergedList.val = list2.val
                    mergedList = mergedList.next
                    list2 = list2.next
                    break
            if list2 == None:
                mergedList = ListNode(list1.val)
                # mergedList.val = list1.val
                list1 = list1.next
        while(list2 != None):
            mergedList = ListNode(list2.val)
            # mergedList.val = list2.val
            list2 = list2.next
        while
        return mergedList


listOne = [1,2,4]
listTwo = [1,3,4]
list1 = None
for i in range(len(listOne)-1,-1,-1):
    list1 = save(list1, listOne[i])

list2 = None
for i in range(len(listTwo)-1,-1,-1):
    list2 = save(list2, listTwo[i])

display(list1)
display(list2)

mergedList = Solution().mergeTwoLists(list1, list2)
display(mergedList)