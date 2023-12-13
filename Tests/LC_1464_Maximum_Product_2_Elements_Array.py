from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p, q = 0,0
        for num in nums:
            if q < num:
                q = num
                if p < q:
                    q,p = p,num
            print(p, q)
        return (p-1)*(q-1)


# nums = [3,4,5,2]
# nums = [1,5,4,5]
# nums = [3,7]
nums = [10,2,5,2]
print(Solution().maxProduct(nums))