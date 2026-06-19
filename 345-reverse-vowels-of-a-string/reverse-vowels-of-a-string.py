class Solution:
    def reverseVowels(self, s: str) -> str:
        lst_vowels=[]
        lst_vowels_index=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                lst_vowels.append(s[i])
                lst_vowels_index.append(i)
            i+=1
        lst_vowels_reverse=list(reversed(lst_vowels))
        for j,m in zip(lst_vowels_index,lst_vowels_reverse):
                s[j]=m
        s="".join(s)
        return s



