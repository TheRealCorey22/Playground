# Problem 53 - Maximum Subarray

# Given an Array of Integers, find the Sum of the Largest Subarray.


# Example: Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

from typing import List
from math import inf

# Test Input
nums = [10,-4,6,-4,3,5-2]



class Solution:

    # Brute Force Method
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize `ans` to a tiny value to ensure any sum found is larger
        ans = -inf

        # Loop through each element of the list as the starting point of the subarray
        for i in range(len(nums)):
            # Initialize `cur_sum` to 0 for each starting point
            cur_sum = 0

            # Loop through each element from the starting point `i` to the end of the list
            for j in range(i, len(nums)):
                # Add the current element to `cur_sum`
                cur_sum += nums[j]
                
                # Update `ans` to be the maximum of the current `ans` or `cur_sum`
                ans = max(ans, cur_sum)
        
        # Return the maximum sum found
        return ans
    

    # Kadane's Algorithm
    def maxSubArrayKadane(self, nums:List) -> int:

        cur_max, max_till_now = 0, -inf

        for c in nums:

            cur_max = max(c, cur_max + c)

            max_till_now = max(max_till_now, cur_max)

        return max_till_now


# Prints Answer - Brute Force Method
print(Solution().maxSubArray(nums))


# Prints Answer - Brute Force Method
print(Solution().maxSubArrayKadane(nums))