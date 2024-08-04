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




# Test Input
s = 'XVI'


class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Key- Pairs
        numerals = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    }
        
        # Initializing Variables
        i = 0
        total = 0
        
        # While Index is Less than Out of Bounds
        while i < len(s) - 1:
            
            # Checks if Value at Current Index is Less than Value at Next Index
            if numerals[s[i]] < numerals[s[i+1]]:

                total -= numerals[s[i]] # Decrements Total by Current Value
                
                i += 1 # Increments Index

            else:

                total += numerals[s[i]] # Increments Total by Current Value
                
                i += 1 # Increments Index
            

        # Increments Total By Current Value
        # This accounts for the last element when exiting the While Loop
        total += numerals[s[i]]

        # Returns Integer
        return total
        

# Prints Answer
print(Solution().romanToInt(s))
