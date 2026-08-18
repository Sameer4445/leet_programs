import math
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            result[i]=prefix
            prefix*=nums[i]

        sufix=1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= sufix
            sufix *= nums[i]

        return result