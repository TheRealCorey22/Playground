# Problem 14 - Longest Common Prefix

# Given a List of Words, Find the Longest Common Prefix

# Example: Flow, Flower, Flight = Fl


from typing import List


strs = ['flower', 'flow', 'flight']


class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        i = 0

        lcp = ''
        

        strs.sort()  # Lexicographical Sorting
        
        
        first = strs[0]

        last = strs[-1]
        
        
        min_length = min(len(first), len(last))
        

        for i in range(min_length):
            
            if first[i] == last[i]:
                
                lcp = lcp + first[i]
                
            else:

                return lcp


print(Solution().longestCommonPrefix(strs))






