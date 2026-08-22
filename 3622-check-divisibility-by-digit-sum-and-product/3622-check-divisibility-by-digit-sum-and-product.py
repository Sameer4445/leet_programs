class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        while n:
            s+=n%10
            p*=n%10
            n//=10
        return True if n%(s+p)==0 else False