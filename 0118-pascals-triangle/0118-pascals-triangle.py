class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    row.append(1)
                else:
                    pre=arr[-1]
                    row.append(pre[j-1]+pre[j])
            arr.append(row)
        return arr
