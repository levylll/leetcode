#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-14 14:30:57

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix


sol = Solution()
a = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
res = sol.setZeroes(a)
print res
