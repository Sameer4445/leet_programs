class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        arr=[]
        for j in h:
            if h[j]>1:
                arr.append(j)
        return arr