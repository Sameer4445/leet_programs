class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        mx=max(arr)
        for i in range(len(arr)):
            if arr[i]==mx:
                return i