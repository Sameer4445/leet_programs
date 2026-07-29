class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dif=0
        ans=0

        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dif+=1
                ans+=dif
            else:
                dif=0
        return ans
