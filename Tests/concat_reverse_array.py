arr = [3,4,5]

def concat(arr,len):
    if len!=0:
        return concat(arr,len-1)*10+arr[len]
    else:return arr[len]

def concat2(arr,len):
    num = 0
    for i in range(len, -1, -1):
        num = num*10+arr[i]
    return num

num = concat(arr,len(arr)-1)
print(num)
num = concat2(arr,len(arr)-1)
print(num)