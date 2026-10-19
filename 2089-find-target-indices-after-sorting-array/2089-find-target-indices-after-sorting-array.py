class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        tarr=[]
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<=target :
            if nums[i]==target:
                tarr.append(i)
            i+=1
        return tarr