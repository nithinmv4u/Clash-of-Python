from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        p=target-nums[i]
        print(p)
        for j in range(i+1,len(nums)):
            print("num: ",nums[j],"p: ",p)
            if p==nums[j]:
                return [i,j]
            
# nums=[2,7,11,15]
# target=26
# nums=[3,2,4]
# target=6
nums = [3,3]
target = 6
print(twoSum(nums,target))