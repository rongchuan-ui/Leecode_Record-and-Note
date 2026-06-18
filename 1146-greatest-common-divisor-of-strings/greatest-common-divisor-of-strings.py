class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        else:
            a= max(len(str1),len(str2))
            b= min(len(str1),len(str2))
            while b:
                c= a%b
                a=b
                b=c
            return str1[:a]
                





        # if str1+str2 != str2+str1:
        #     return ""
        # a= max(len(str1),len(str2))
        # b= min(len(str1),len(str2))
        # def innergcd(a,b):
        #     if not b:
        #         return a
        #     return innergcd(b,a%b)
        # gcd_len = innergcd(a, b)
        # return str1[:gcd_len]