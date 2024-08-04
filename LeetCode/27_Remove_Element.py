# Problem 27 - Remove Element

# Remove Value from Array(In-Place), Return n Nums that aren't equal to Value.

# Example: input = [2,3,3,2], target = 3
# n = 2 [3,3]


from typing import List # Hint

# Test Inputs
nums = [0,1,2,2,3,0,4,2]
val = 2



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Initialize Variable
        i = 0
        
        # Loops Until Index is Equal to Input Length
        while i < len(nums):
            
            # Checks if List at Current Index is Equal to Target Value
            if nums[i] == val:
                
                # Removes Element at Current Index
                nums.pop(i)
                
            else:
                
                # Increments Index
                i += 1
        return len(nums)


print(Solution().removeElement(nums, val))


  



