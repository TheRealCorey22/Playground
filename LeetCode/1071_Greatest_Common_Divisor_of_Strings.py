# Problem 1071 - Greatest Common Divisor of Strings

# Description:
# Find the Greatest Common Divisor between Strings.

# Example 1:
# Input: string1['ABCABC'], string2['ABC']
# Output: "ABC"

# Example 2:
# Input: string1['ABABAB'], string2['AB']
# Output: "AB"


str1 = 'ABABAB'
str2 = 'ABAB'


class Solution:
    

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        str1 = list(str1)
        str2 = list(str2)
        
        while str1 and str2:
            
            if str1[0] == str2[0]:
                
                str1.pop(0)
                
                str2.pop(0)
                
            else:
                return ("")


        if str1:
            
            str1 = ''.join(str1)
            
            return str1
    
        if str2:
            
            str2 = ''.join(str2)
            
            return str2
    

print(Solution().gcdOfStrings(str1, str2))

