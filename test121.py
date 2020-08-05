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
        n_max = None
        res = 0
        if prices:
            n_min = prices[0]
        for elem in prices:
            if n_min < elem:
                if res < (elem - n_min):
                    res = elem - n_min
            else:
                n_min = elem
        return res


so = Solution()
# a = [7,1,5,3,6,4]
a = [2,1,2,1,0,1,2]
res = so.maxProfit(a)
print res


