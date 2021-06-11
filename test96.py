#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-05-25 19:43:07

from collections import defaultdict
class Solution(object):

    def __init__(self):
        self.record = defaultdict(int)


    def process(self, n):
        if n == 1 or n == 0:
            self.record[n] = 1
            return

        res = 0
        for i in range(n):
            # print i, n-i, self.record[i], self.record[n-i-1]
            res += self.record[i] * self.record[n-i-1]
        self.record[n] = res


    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(0, n+1):
            self.process(i)

        return self.record[n]




n = 3
sol = Solution()
print sol.numTrees(n)
