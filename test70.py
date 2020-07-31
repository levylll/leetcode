#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-13 16:52:34


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        i1 = 1
        i2 = 2
        for i in range(3, n+1):
            tmp = i1 + i2
            i1 = i2
            i2 = tmp
        return i2

sol = Solution()
res = sol.climbStairs(3)
print res
