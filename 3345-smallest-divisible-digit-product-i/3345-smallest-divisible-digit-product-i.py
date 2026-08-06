class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        curr=n
        while(True):
            temp=curr
            pro=1
            while(temp>0):
                pro*=temp%10
                temp//=10

            if pro%t==0:
                return curr
            curr+=1