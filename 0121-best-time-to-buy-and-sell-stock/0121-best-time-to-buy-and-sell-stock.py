class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p=prices[0]
        price=0

        for p in prices:
            min_p=min(min_p,p)
            price=max(price,p-min_p)

        return price