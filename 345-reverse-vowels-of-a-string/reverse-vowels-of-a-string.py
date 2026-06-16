class Solution:
    def reverseVowels(self, s: str) -> str:
        lst_vowels=[]
        lst_vowels_index=[]
        s=list(s)
        m=0
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                lst_vowels.append(s[i])
                lst_vowels_index.append(i)
            i+=1
        lst_vowels_reverse=list(reversed(lst_vowels))
        for j in lst_vowels_index:
                s[j]=lst_vowels_reverse[m]
                m+=1
        s="".join(s)
        return s



