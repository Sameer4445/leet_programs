class Solution:
    def frequencySort(self, s: str) -> str:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        sorted_char=sorted(h,key=h.get,reverse=True)

        ans=""
        for i in sorted_char:
            ans+=i*h[i]
        return ans