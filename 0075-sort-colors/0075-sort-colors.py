class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        # Count frequency of 0s, 1s and 2s
        for num in nums:
            count[num] += 1

        # Overwrite the original array
        idx = 0

        for _ in range(count[0]):
            nums[idx] = 0
            idx += 1

        for _ in range(count[1]):
            nums[idx] = 1
            idx += 1

        for _ in range(count[2]):
            nums[idx] = 2
            idx += 1