# Problem 13 - Roman To Integer

# Given a Roman Numeral, Convert it to an Integer.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Example: IV = 4, VI = 6


s = 'XVI'


class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        
        numerals = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    }
        
        
        i = 0

        total = 0

        
        while i < len(s) - 1:
            
            if numerals[s[i]] < numerals[s[i+1]]:

                total -= numerals[s[i]]
                
                i += 1

            else:

                total += numerals[s[i]]
                
                i += 1


        total += numerals[s[i]]

        return total
        

print(Solution().romanToInt(s))
