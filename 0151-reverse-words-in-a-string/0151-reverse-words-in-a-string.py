class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j=s.split()
        return " ".join(j[::-1])