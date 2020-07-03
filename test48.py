#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-04-27 15:36:17

class Solution(object):

    def change_v(self, matrix, ai, aj, bi, bj):
        t = matrix[ai][aj]
        matrix[ai][aj] = matrix[bi][bj]
        matrix[bi][bj] = t

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)/2+1):
            for j in range(len(matrix)/2+1):
                self.change_v(matrix, i, j, i, len(matrix) - j - 1)
                self.change_v(matrix, i, len(matrix) - j - 1, len(matrix) - i - 1, len(matrix) - j - 1)
        return matrix


s = Solution()
matrix = [[ 5, 1, 9,11],
[2, 4, 8,10],
[13, 3, 6, 7],
[15,14,12,16]]

print s.rotate(matrix)


