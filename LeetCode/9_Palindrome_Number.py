# Problem 9 - Palindrome Number

# Description:
# Given an Integer, Check if its a Palindrome.

# Example 1:
# Input: 123 
# Output: False

# Example 2:
# Input: 121
# Output: True


x = 121


class Solution:
    
    def isPalindromeString(self, x: int) -> bool:  # String Method
        

        x = str(x)
        

        reverse_x = x[::-1]  # Reverses Via Slicing
        

        if x == reverse_x:
            return True

        else:
            return False


    def isPalindromeArithmetic(self, x:int) -> bool:  # Arithmetic Method
    

        temp = x 
        reverse_x = 0


        if x < 0:  # Hedge Case: (-) Makes a String Asymmetrical.
            return False


        while temp != 0:
            
            digit = temp % 10  # Gets Last Number of Integer

            reverse_x = reverse_x * 10 + digit  # Builds New Integer

            temp //= 10  # Allows Loop to Become 0


        if reverse_x == x:
            return True
        
        else:
            return False


print(Solution().isPalindromeString(x))

print(Solution().isPalindromeArithmetic(x))


