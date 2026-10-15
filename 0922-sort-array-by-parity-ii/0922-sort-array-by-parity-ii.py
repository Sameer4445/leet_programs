class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        l=0
        r=1
        while l<len(nums) and r<len(nums):
            if nums[l]%2==0:
                l+=2
            elif nums[r]%2!=0:
                r+=2
            else:
                nums[l],nums[r]=nums[r],nums[l]
        return nums