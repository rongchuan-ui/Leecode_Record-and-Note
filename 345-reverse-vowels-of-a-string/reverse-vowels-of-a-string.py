# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         lst_vowels=[]
#         lst_vowels_index=[]
#         s=list(s)
#         for i in range(len(s)):
#             if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
#                 lst_vowels.append(s[i])
#                 lst_vowels_index.append(i)
#             i+=1
#         lst_vowels_reverse=list(reversed(lst_vowels))
#         for j,m in zip(lst_vowels_index,lst_vowels_reverse):
#                 s[j]=m
#         s="".join(s)
#         return s

class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. 用 hash set（集合）代替列表，查找复杂度从 O(N) 降到 O(1)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # 左指针找元音
            while left < right and s[left] not in vowels:
                left += 1
            # 右指针找元音
            while left < right and s[right] not in vowels:
                right -= 1
            
            # 找到后原地交换，并移动指针
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return "".join(s)



