#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-04-27 15:36:17

class Solution(object):

    def transport1(self, matrix):
        # 转置
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if i == j:
                    continue
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        return matrix

    def transport2(self, matrix):
        # 转置
        m_len = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)/2):
                # print j
                t = matrix[i][j]
                matrix[i][j] = matrix[i][m_len-j-1]
                matrix[i][m_len-j-1] = t
        return matrix

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transport1(matrix)
        matrix = self.transport2(matrix)
        return matrix


s = Solution()
matrix = [[ 5, 1, 9,11],
[2, 4, 8,10],
[13, 3, 6, 7],
[15,14,12,16]]

print s.rotate(matrix)


