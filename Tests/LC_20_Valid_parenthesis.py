class Solution:
    def isValid(self, s):
        parentheses_mapping = {'(': ')', '{': '}', '[': ']'}
        parentheses_list = []
        for p in s:
            if p in "{[(":
                if p in parentheses_mapping:
                    p= parentheses_mapping[p]
                    parentheses_list.append(p)
            elif p in "}])":
                print(len(parentheses_list))
                if len(parentheses_list) and parentheses_list[len(parentheses_list)-1]==p:
                    parentheses_list = parentheses_list[:len(parentheses_list)-1]
                else: return False
            print(parentheses_list)
        return False if len(parentheses_list) else True

s = "[{()}]"
# s = "()[]{}"
# s = "{[]}"
# s="]"
# s="(])"

print(Solution().isValid(s))



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def push(node, value):
#     newNode = Node(value)
#     newNode.next = node
#     return newNode

# def pop(node):
#     temp = node
#     node = node.next
#     temp = None
#     return node

# class Solution:
#     def isValid(self, s):
#         parentheses_mapping = {'(': ')', '{': '}', '[': ']'}
#         node = None
#         for p in s:
#             if p in "{[(":
#                 print("opening: ",p)
#                 if p in parentheses_mapping:
#                     p = parentheses_mapping[p]
#                 node = push(node, p)
#             elif p in "}])":
#                 print("closing: ",p)
#                 if node != None and node.value==p:
#                     print("match", node.value, p)
#                     node = pop(node)
#                 else: return False
#             node_test = node
#             while node_test != None:
#                 print(node_test.value)
#                 node_test=node_test.next
#         return True if node is None else False

# s = "[{()}]"
# s = "()[]{}"
# s = "{[]}"
# s="]"
# # s="(])"

# print(Solution().isValid(s))












# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def insert(node, data):
#     newNode = Node(data)
#     newNode.next = node
#     return newNode

# if __name__ == '__main__':
#     # data = input("Enter number: ")
#     list1 = "(){}[]"
#     node = None
#     for num in list1:
#         node = insert(node, num)
#     while node != None:
#         print(node.data)
#         node=node.next













# # para = "[{()}]"
# para = "()[]{}"
# # para = "{[]}"


# def check(para, i=0):
#     print(f"para[i]: {para[i]}  para[i+1]: {para[i+1]}  i: {i}   half length: {len(para)//2} compare: {para[i]!=para[i+1]}")
#     c=''
#     if para[i]=='[':c=']'
#     if para[i]=='{':c='}'
#     if para[i]=='(':c=')'
#     if c!=para[i+1] and i <= len(para)//2:
#         valid = False
#         print(f"failed valid: {valid}")
#         check(para, i+1)
#     elif c==para[i+1] and i <= len(para)//2:
#         valid = True
#         print(f"success valid: {valid}")

#     print(f"len: {len(para) }  c: {c} para[len(para)-(len(para)-(i+1))]: {para[len(para)-(i+1)]}  i: {i}   len(para)-(i+1):{len(para)-(i+1)}")
#     if c==para[len(para)-(i+1)]:
#         valid = True
#         print(f"valid: {valid}")
#         try:check(para, i+2)
#         except:pass
#     else:
#         valid = False
#         print(f"valid: {valid}")
#     return valid

# valid = check(para, 0)
# print(valid)