class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==self.digitsum(nums[i]):
                return i
        return -1
    def digitsum(self,a):
        s=0
        while(a>0):
            s+=a%10
            a//=10
        return s