class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        arr=[]
        for i in h:
            if h[i] > len(nums)//3:
                arr.append(i)
        return arr

