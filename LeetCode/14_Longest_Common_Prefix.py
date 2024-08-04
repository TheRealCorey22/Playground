# Problem 14 - Longest Common Prefix

# Given a List of Words, Find the Longest Common Prefix

# Example: Flow, Flower, Flight = Fl



from typing import List


# Test Input
strs = ['flower', 'flow', 'flight']


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        # Initializes Variables
        i = 0
        lcp = ''
        

        # Lexicographically Sorts
        strs.sort()
        
        
        first = strs[0] # Assigns First Element
        last = strs[-1] # Assigns Last Element
        
        
        # Assigns the Shorter Element
        min_length = min(len(first), len(last))
        

        # Iterates through Each Element
        for i in range(min_length):
            
            # Checks if the same index as the same value.
            if first[i] == last[i]:
                
                # If so, add that value to our Longest Common Prefix
                lcp = lcp + first[i]
                
                # Otherwise, Return What We Have! Party is Over!
            else:
                return lcp

# Prints Answer
print(Solution().longestCommonPrefix(strs))






