#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-14 14:30:57

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col1 = False
        row1 = False
        top1 = False
        for j in range(0, len(matrix[0])):
            for i in range(0, len(matrix)):
                if i == 0 and j == 0:
                    if matrix[i][j] == 0:
                        top1 = True
                    continue
                if matrix[i][j] == 0:
                    if i == 0:
                        row1 = True
                    if j == 0:
                        col1 = True
                    if i != 0 and j != 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for j in range(1, len(matrix[0])):
            for i in range(1, len(matrix)):

                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if row1 == True or top1 == True:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if col1 == True or top1 == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix


sol = Solution()
a = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
res = sol.setZeroes(a)
print res

a = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]]
res = sol.setZeroes(a)
for i in res:
    print i

print '========'
a = [
    [1,1,1],
    [0,1,2]]
res = sol.setZeroes(a)
for i in res:
    print i

print '========'
a = [
    [-4,-2147483648,6,-7,0],
    [-8,6,-8,-6,0],
    [2147483647,2,-9,-6,-10]]
res = sol.setZeroes(a)
for i in res:
    print i
