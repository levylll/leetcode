#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-08 15:27:08

class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        total = len(matrix) * len(matrix[0])
        i, j, di, dj = 0, 0, 0, 1
        res = []
        for _ in range(total):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i+di)%len(matrix)][(j+dj)%len(matrix[0])] == None:
                di, dj = dj, -di
            i += di
            j += dj
        return res


so = Solution()
a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
res = so.spiralOrder(a)
assert res == [1,2,3,6,9,8,7,4,5]



a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
res = so.spiralOrder(a)
assert res == [1,2,3,4,8,12,11,10,9,5,6,7]

a = []
res = so.spiralOrder(a)
assert res == []
