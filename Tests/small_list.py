arr=[3,2,4,1,5]
min=arr[0]
for i in range(4):
    if(min>arr[i+1]):
        min=arr[i+1]
    # else:min=arr[i+1]
print(min)