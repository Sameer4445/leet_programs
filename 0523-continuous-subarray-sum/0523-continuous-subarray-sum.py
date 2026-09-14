class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        arr=[nums[0]]
        for i in range(1,len(nums)):
            arr.append(arr[i-1]+nums[i])
        rem={0:-1}
        for i in range(len(arr)):
            r = arr[i] % k

            if r in rem:
                if i - rem[r] >= 2:
                    return True
            else:
                rem[r] = i

        return False