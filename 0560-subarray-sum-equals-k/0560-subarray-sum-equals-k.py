class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        prefix=0

        dic={
            0:1
        }

        for i in nums:
            prefix+=i
            need=prefix-k
            if need in dic:
                count+=dic[need]
            if prefix in dic:
                dic[prefix]+=1
            else:
                dic[prefix]=1
        return count