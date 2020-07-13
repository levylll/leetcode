#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-13 13:25:31

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1
        elif n == 1:
            return 1
        else:
            step1 = self.uniquePaths(m -1, n)
            step2 = self.uniquePaths(m, n-1)
            return step1 + step2

sol = Solution()
m = 3
n = 2
res = sol.uniquePaths(m, n)
assert res == 3

m = 1
n = 1
res = sol.uniquePaths(m, n)
assert res == 1

m = 23
n = 12
res = sol.uniquePaths(m, n)
assert res == 1
