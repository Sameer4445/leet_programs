class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s=0.00
        mx=0.00

        for i in range(k):
            s+=nums[i]
        mx=s
        for i in range(k,len(nums)):
            s-=nums[i-k]
            s+=nums[i]
            mx=max(mx,s)
        return mx/k