def binary_search(arr, x, low, high):
	if low > high:
		return -1
	else:
		mid = ((high-low) + low) // 2
		if arr[mid] > x:
			return binary_search(arr, x, low, mid-1)                                                 
		elif arr[mid] < x:
			return binary_search(arr, x, mid+1, high)
		else: 
			return mid


arr = [ 2, 3, 4, 10, 40, 50 ]
x = 4 


result = binary_search(arr, x, 0, len(arr)-1)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")