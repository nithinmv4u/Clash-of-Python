class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = [num for num in nums if num != val] # ----- not working in leetcode
        # for num in nums
        print(nums)

# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
Solution().removeElement(nums, val)
print(nums)