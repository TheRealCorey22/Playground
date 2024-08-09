# Problem 27 - Remove Element

# Description:
# Remove Value from Array(In-Place), Return n Nums that aren't equal to Value.

# Example:
# Input: Array[2,3,3,2], target = 3
# n = 2 [3,3]


from typing import List # Hint


nums = [0,1,2,2,3,0,4,2]
val = 2


class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:


        i = 0
        
        
        while i < len(nums):
            
            if nums[i] == val:
                
                nums.pop(i)
                
            else:
                
                i += 1


        return len(nums)


print(Solution().removeElement(nums, val))


  



