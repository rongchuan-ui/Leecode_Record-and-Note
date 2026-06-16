class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=[] 
        m=min(len(word1),len(word2))
        for i in range(0,m):
            word3.append(word1[i])
            word3.append(word2[i])
        n=max(len(word1),len(word2))
        if n>len(word1):
            word3.extend(word2[m:])
        else:
            word3.extend(word1[m:])
        word3="".join(word3)
        return word3


       