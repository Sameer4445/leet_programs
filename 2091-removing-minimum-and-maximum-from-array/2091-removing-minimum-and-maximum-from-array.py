class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn=min(nums)
        mx=max(nums)
        n=len(nums)

        i=nums.index(mn)
        j=nums.index(mx)

        front = max(i,j)+1
        back = n-min(i,j)
        fb = min(i,j)+1 + n-max(i,j)

        return min(front,back,fb)