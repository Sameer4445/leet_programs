class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=nums[i]+pre[i-1]
        return pre