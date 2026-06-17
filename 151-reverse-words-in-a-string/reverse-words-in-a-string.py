class Solution:
    def reverseWords(self, s: str) -> str:
        step1=s.split()
        step2=step1[::-1]
        step3=" ".join(step2)
        return step3

    

        
        