list1 = [3,2,1]

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
def save(node,value):
    newnode=ListNode(value)
    newnode.next = node
    return newnode
class Solution:
    def swapPairs(self, head):
        if(head is not None):
            p=head.next
        while(head!=None):
            a = head
            head=head.next
            if(head is not None):
                b=head.next
                if head.next is not None and head.next.next is not None:
                    a.next = head.next.next
                else:
                    a.next = b
                head.next = a
                head=b
        return p

if __name__ == '__main__':
    l1 = None
    for i in range(len(list1)):
        l1 = save(l1, list1[i])
    # while(l1!=None):
    #     print(l1.val)
    #     l1=l1.next
    s=Solution()
    l1=s.swapPairs(l1)
    print(l1)
    while(l1!=None):
        print(l1.val)
        l1=l1.next
    # while(swaped_l1!=None):
    #     print(swaped_l1.val)
    #     swaped_l1=swaped_l1.next
