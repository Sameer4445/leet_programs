class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        tarr=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                tarr.append(i)
        return tarr