# Problem 1 - Two Sum

# Description:
# Given an Array of numbers, return the indices whose values add to Target.

# Example:
# Input: Array[1,4,3,3], Target[5]
# Output: [0,1]


from typing import List


nums = [1,2,3,4]

target = 6


class Solution:

    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:  # Brute Force Method

        for i in range(len(nums)):

            for j in range(len(nums)):

                if nums[i] + nums[j] == target:
                    return [i,j]
                
        return []
 
 
    def twoSumHash(self, nums: List[int], target: int) -> List[int]: # Hash Method

        
        hash_table = {}


        for index, num in enumerate(nums):

            key = target - num
            
            if key in hash_table:

                return [hash_table[key], index] 
            
            else:
                hash_table[num] = index 
    

        return []
    


print(Solution().twoSumBrute(nums,target))

print(Solution().twoSumHash(nums,target))


