class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        mx=0
        ss=set()

        for i in range(len(s)):
            while s[i] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[i])
            mx=max(mx,i-l+1)
        return mx
