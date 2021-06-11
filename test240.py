#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-06-08 13:34:35

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        col = len(matrix[0])

        m = row - 1
        n = 0
        while m >= 0 and n < col:
            print m, n
            if matrix[m][n] == target:
                return True

            if matrix[m][n] > target:
                m -= 1
                continue

            if matrix[m][n] < target:
                n += 1

        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
matrix = [[-5]]
target = -5

sol = Solution()
res = sol.searchMatrix(matrix, target)
print res
