first = 1
second = 1
result = [1] * len(nums)
print(result)
for i in range(len(nums)):
    result[i]= first* result[i]
    first = first * nums[i]
    result[len(nums)-i-1] = second
    second =second * nums[len(nums)-i-1]
    # print(first, second)
    print(result)