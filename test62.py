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
        dp = [[1]*(n)]*(m)
        if m == 1 or n == 1:
            return 1
        else:
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

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
print res
# assert res == 1
