

word1 = 'abc'
word2 = 'pqrx'



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        word3 = ''

        word1 = list(word1)
        word2 = list(word2)


        while word1 and word2:


            word3 += word1[0]
            word1.pop(0)

            word3 += word2[0]
            word2.pop(0)

        
        word1 = "".join(word1)
        word2 = "".join(word2)


        if word1:
            
            word3 += word1

        if word2:

            word3 += word2

        return word3
    


print(Solution().mergeAlternately(word1,word2))







"""
word1 = 'abc'
word2 = 'pqr'
word3 = ''

word1 = list(word1)
word2 = list(word2)
word3 = list(word3)


word3 += word1[0]
word1.pop(0)
word3 += word2[0]
word2.pop(0)


word3 += word1[0]
word1.pop(0)
word3 += word2[0]
word2.pop(0)


word3 += word1[0]
word1.pop(0)



word1 = "".join(word1)
word2 = "".join(word2)




if word1:
    word3.append(word1)

if word2:
    word3.append(word2)

print(word3)
"""