class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minNo=min(nums)
        maxNo=max(nums)
        arr=[]
        for i in range(minNo,maxNo):
            if i not in nums:
                arr.append(i)
        return arr