# Problem 53 - Maximum Subarray

# Description:
# Given an Array of Integers, find the Sum of the Largest Subarray.

# Example: Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


from typing import List
from math import inf


nums = [10,-4,6,-4,3,5-2]


class Solution:

    def maxSubArrayBrute(self, nums: List[int]) -> int:  # Brute Force Method


        ans = -inf


        for i in range(len(nums)):

            cur_sum = 0

            for j in range(i, len(nums)):

                cur_sum += nums[j]
                
                ans = max(ans, cur_sum)
        
        
        return ans
    
    
    def maxSubArrayKadane(self, nums:List) -> int:  # Kadane's Algorithm


        cur_max, max_till_now = 0, -inf


        for num in nums:

            cur_max = max(num, cur_max + num)

            max_till_now = max(max_till_now, cur_max)

        
        return max_till_now


print(Solution().maxSubArrayBrute(nums))

print(Solution().maxSubArrayKadane(nums))