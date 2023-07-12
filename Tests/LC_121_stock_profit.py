arr = [7,1,5,3,6,4]
min = 0
max_profit = 0
for i in range(len(arr)):
    if arr[min]>arr[i]:
        min = i
    diff = arr[i]-arr[min]
    if diff>max_profit:
        max_profit = diff
        max = i

print(max_profit)
print(arr[min])
print(arr[max])