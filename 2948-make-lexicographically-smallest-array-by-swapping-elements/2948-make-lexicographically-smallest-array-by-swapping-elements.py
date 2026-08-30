class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)

        pairs = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * n

        i = 0

        while i < n:
            j = i

            while (
                j + 1 < n
                and pairs[j + 1][0] - pairs[j][0] <= limit
            ):
                j += 1

            indices = []
            values = []

            for k in range(i, j + 1):
                values.append(pairs[k][0])
                indices.append(pairs[k][1])

            indices.sort()

            for idx, val in zip(indices, values):
                ans[idx] = val

            i = j + 1

        return ans