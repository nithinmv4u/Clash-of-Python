arr = [2,-1,-2,3,-5,6,1]

min = 0
for i in range(len(arr)):
    diff = 0-arr[i]
    if diff<0:diff = -diff
    min_val = 0-arr[min]
    if min_val<0:min_val = -min_val
    if arr[min]==-arr[i]:
        if arr[min]<arr[i]:min = i
    elif min_val>diff:min = i
    print(f"min val: {min_val}, diff: {diff}, arr[min]: {arr[min]}")

print(arr[min])