# Problem 53 - Maximum Subarray

# Given an Array of Integers, find the Sum of the Largest Subarray.


# Example: Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

from typing import List


nums = [3,4,-3,2,-3]

class Solution:

    def maxSubArray(self, nums: List) -> int:
    # Initialize current_sum and max_sum with the first element of the list
        current_sum = nums[0]
        max_sum = nums[0]

        # Iterate through list starting from the second element
        for num in nums[1:]:

        # Update current_sum to become the maximum of num or current_sum + sum
            current_sum = max(num, current_sum + num)
    
            # Update max_sum to be the maximum of max_sum or the current_sum
            max_sum = max(max_sum, current_sum)

            return(max_sum)
        
# Prints Answer
print(Solution().maxSubArray(nums))
