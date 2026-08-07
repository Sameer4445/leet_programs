class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        left_sum=0
        for i in nums:
            tot+=i
        
        for i in range(len(nums)):
            right_sum=tot - left_sum - nums[i]
            if(left_sum==right_sum):
                return i
            else:
                left_sum +=nums[i]
        return -1