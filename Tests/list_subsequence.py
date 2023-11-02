# def subsequence(my_list, seq_list=[]):
#     new_list =[]
#     for i in range(len(my_list)-1):
#         print(i, my_list[i+1])
#         if my_list[i] < my_list[i+1]:
#             new_list.append(my_list[i])
#             continue
#         new_list.append(my_list[i])
#         if len(seq_list) < len(new_list):
#             seq_list = new_list
#             i=-1
#         new_list = []
#     return seq_list

def subsequence(my_list, seq_list=[]):
    new_list = []
    i=0
    for i in range(len(my_list)-1):
        if my_list[i] < my_list[i+1]:
            new_list.append(my_list[i])
        else:
            new_list.append(my_list[i])
            break
    print("new list: ",new_list)
    if len(new_list) > len(seq_list):
        seq_list = new_list
    print(my_list[i+1:],seq_list,len(my_list))
    if len(my_list):
        return subsequence(my_list[i+1:], seq_list)
    else:
        print("else", seq_list)
        return seq_list
        

my_list = [1, 3, 2, 4, 5, 7, 6, 8]

result = subsequence(my_list)

print("result: ",result)