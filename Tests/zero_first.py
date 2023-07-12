arr = [0,3,0,4,0,5,7,0]
count =0

for i in range(len(arr)):
    if arr[i]==0:
        count +=1
        for j in range(i, 0, -1):
            arr[j],arr[j-1]=arr[j-1],arr[j]

print(arr)
print(f"count: {count}")