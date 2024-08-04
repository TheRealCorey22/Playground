# Problem 1 - Two Sum

# Given an Array of Numbers, Return the Indices of Numbers Which Add to Target Value.

# Example: Input = [1,4,3,3], Target = 5
# 1 + 4 = 5
# Return [0,1]



from typing import List # Hints



# Test Inputs
nums = [1,2,3,4]
target = 4



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initializes Dictionary for Key-Pairs
        hash_table = {}


        # Iterates through Array & Assigns Index to Each Element Via Enumeration
        for index, num in enumerate(nums):

            # Calculation to Create Key
            key = target - num
            
            # Checks for Key in Table.
            if key in hash_table:
                return [hash_table[key], index] # Returns Key's Corresponding Index and Current Elements Index
            
            # Adds Current Key-Pair to hash_table as it wasn't already found.
            else:
                hash_table[num] = index 

        # Returns an Empty List Incase There's No Valid Answer.
        return []


# Prints Solution
print(Solution().twoSum(nums,target))

