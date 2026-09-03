class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        od=-1
        for i in nums1:
            if i % 2 ==1:
                od=i
                break
        if od==-1:
            return True
        elif min(nums1)%2==1:
            return True
        else:
            return False