class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {0: -1}
        prefix = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in mp:
                ans = max(ans, i - mp[prefix])
            else:
                mp[prefix] = i

        return ans