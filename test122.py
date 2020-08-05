#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-04 16:03:41

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n_min = None
        res = 0
        if prices:
            n_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                if prices[i-1] > n_min:
                    res+=(prices[i-1] - n_min)
                n_min = prices[i]
                continue
            elif i == len(prices) - 1:
                if prices[i] > n_min:
                    res+=(prices[i] - n_min)
            if prices[i] < n_min:
                n_min = prices[i]
        return res


so = Solution()
# a = [7,1,5,3,6,4]
# a = [2,1,2,1,0,1,2]
a = [7,1,5,3,6,4]
res = so.maxProfit(a)
print res


