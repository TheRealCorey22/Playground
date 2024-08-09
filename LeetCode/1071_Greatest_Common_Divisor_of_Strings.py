# Problem 1071 - Greatest Common Divisor of Strings

# Description:
# Find the Greatest Common Divisor between Strings.

# Example 1:
# Input: string1['ABCABC'], string2['ABC']
# Output: "ABC"

# Example 2:
# Input: string1['ABABAB'], string2['AB']
# Output: "AB"

from math import gcd


str1 = 'ABCABC'
str2 = 'ABC'


class Solution:
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        if str1 + str2 != str2 + str1:
            
            return("")
            
        else:
            
            return(str1[:gcd(len(str1), len(str2))])

      
print(Solution().gcdOfStrings(str1, str2))




  






