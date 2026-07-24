class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s=nums1+nums2
        s.sort()
        n=len(s)

        if n%2!=0:
            return s[n//2]
        else:
            
            return (s[n//2 - 1] + s[n//2]) / 2.00
