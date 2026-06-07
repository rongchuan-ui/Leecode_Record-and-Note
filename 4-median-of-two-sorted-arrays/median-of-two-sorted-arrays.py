import math
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        # a=(len(nums1)+1)//2
        # nums1[a]
        #return nums1
        m=len(nums1)
        n=m%2
        b=int(m/2)
        if n == 0:
            return (nums1[b-1]+nums1[b])/2
        else:
            return nums1[math.floor(m/2)]
