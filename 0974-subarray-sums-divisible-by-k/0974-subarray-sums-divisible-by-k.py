class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rem=[0]*k
        offset=0
        res=0

        for cur in nums:
            offset=(offset+cur)%k
            rem[(cur%k-offset)%k]+=1
            res+=rem[(-offset)%k]
        return res