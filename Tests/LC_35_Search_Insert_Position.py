from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high+low)//2
            print(high,low)
            print(mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
            # print(high,low)
        return high+1

# nums = [1,3,5,6]
# target = 5
# nums = [1,3,5,6]
# target = 2
nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))