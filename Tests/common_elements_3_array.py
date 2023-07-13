#both common_element working

# def common_element(arr,common):
#     for num in arr:
#         if num in common:
#             common[num] += 1
#         else:
#             common[num] = 1
#     return common

def common_element(arr,common):
    for i in range(len(arr)):
        if arr[i] in common:
            common[arr[i]]+=1
        else: common[arr[i]]=1
    return common

common ={}
for _ in range(3):
    arr = list(map(int,input("Enter Array: ").strip().split()))
    common=common_element(arr,common)

print(common)
# for num in common:
#     if common[num]==3:
#         print(num, end=' ')
num=[num for num in common if common[num]==3]
print(num)