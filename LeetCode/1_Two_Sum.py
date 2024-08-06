# Problem 1 - Two Sum

# Given an Array of Numbers, Return the Indices of Numbers Which Add to Target Value.

# Example: Input = [1,4,3,3], Target = 5
# 1 + 4 = 5
# Return [0,1]


from typing import List


nums = [1,2,3,4]

target = 4


class Solution:
    
    def twoSumHash(self, nums: List[int], target: int) -> List[int]: # Hash Method

        
        hash_table = {}


        for index, num in enumerate(nums):

            key = target - num
            
            if key in hash_table:

                return [hash_table[key], index] 
            
            else:
                hash_table[num] = index 
    

        return []


print(Solution().twoSumHash(nums,target))

