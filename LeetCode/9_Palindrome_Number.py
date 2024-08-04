# Problem 9 - Palindrome Number

# Given an Integer, Check if it's the same forwards and backwards.

# Example: 123 becomes 321
# 123 isn't the same as 321, thusly isn't a palindrome.




# Test Input
x = 121


class Solution:

    # String Method
    def isPalindromeString(self, x: int) -> bool:
        
        # Converts Integer to String
        x = str(x)
        
        # Reverses String Via Slicing
        reverse_x = x[::-1]
        
        # Compares Original to Reversed
        if x == reverse_x:
            return True

        else:
            return False
        



    # Arithmetic Method
    def isPalindromeArithmetic(self, x:int) -> bool:
    
        # Initializes Variavbles
        temp = x 
        reverse_x = 0

        # Hedge Case - Negative Inputs Are Never Palindromes.
        if x < 0:
            return False

        # Loops Until Temp Becomes 0
        while temp != 0:
            
            # Takes Last Number within Input and Assigns it to Digit.
            digit = temp % 10

            # Builds Number Back Up In Reverse.
            reverse_x = reverse_x * 10 + digit

            # Rounds Down Input Toward 0
            temp //= 10


        # Compares Original to Reversed
        if reverse_x == x:
            return True
        
        else:
            return False



     
# Prints Answer - String Method
print(Solution().isPalindromeString(x))


# Prints Answer - Arithmetic Method
print(Solution().isPalindromeArithmetic(x))


