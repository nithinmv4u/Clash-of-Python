# def sum_numbers(*args):
#     result=0
#     num=[]
#     num=list(args)
#     # num=[1,2,3,4,5]
#     print(type(num))
#     for i in num:
#         # result+=i
#         print('hi',i)
#     return result

# a=[2,3,4,5,6,7]
# print(type(a))
# # sum_numbers(a)
# print(sum_numbers(a))

# thislist = [1,2,3,4,5]
# result=0
# for x in thislist:
#     result+=x
# print(result)



def summation(*test_tup):
  # converting into list
    test = list(*test_tup)
 
    # initializing count
    count = 0
 
    # for loop
    for i in test:
        count += i
    return count
 
 
# initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))