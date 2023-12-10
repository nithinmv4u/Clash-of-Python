# class Solution(object):
#     def removeDuplicates(self, nums):
#         i = 0
#         length = len(nums)
#         j = 1
#         print(length)
#         while i+j < length:
#             print(i)
#             if nums[i] == nums[i+j]:
#                 j+=1
#                 continue
#             nums[i+1] = nums[i+j]
#             i+=1
#         print(nums, i, j, length)

class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
        print(nums, i)


nums = [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9]
# nums = [1,1,2]
Solution().removeDuplicates(nums)
# sorted_list[2], sorted_list[3] = sorted_list[3], sorted_list[2]

# print(sorted_list)