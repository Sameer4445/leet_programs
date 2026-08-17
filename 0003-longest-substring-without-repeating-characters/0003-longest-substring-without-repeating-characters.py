class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        mx=0
        new=set()
        for i in s:
            while(i in new):
                new.remove(s[left])
                left+=1
            new.add(i)
            length=len(new)
            mx=max(length,mx)
        return mx
        