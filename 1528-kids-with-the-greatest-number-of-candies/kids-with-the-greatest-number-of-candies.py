class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst=[]
        m=max(candies)
        for i in range(0, len(candies)):
            n=extraCandies+candies[i]
            if m>n:
                # lst.append(bool(0))
                lst.append(False)
            else:
                # lst.append(bool(1))
                lst.append(True)
        return lst