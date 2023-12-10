def remove_duplicate(nums):
    i=0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i+1])
        else:
            i+=1
    print(nums)

sorted_list = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9]
remove_duplicate(sorted_list)