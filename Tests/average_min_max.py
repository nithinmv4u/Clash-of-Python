nums = [4,1,4,0,3,5]
travel = len(nums)/2
min = nums[0]
max = nums[0]
prev_min = 0
prev_max = 0
for i in range(len(nums)):
    if min>prev_min and min>nums[i]:
        min = nums[i]
    # if max<prev_max and max<nums[i]:
        