class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        val=0
        
        if(k%2==0 or k%5==0):
            return -1
        else:
            for i in range(1,k+1):
                val=(val*10+1)%k
                if val==0:
                    return i
                
            return -1

        