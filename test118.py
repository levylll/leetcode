#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-04 15:31:25

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for row_len in range(1, numRows+1):
            tmp_list = []
            for i in range(row_len):
                if i == 0 or i == row_len - 1:
                    tmp_list.append(1)
                else:
                    tmp_list.append(res[-1][i-1] + res[-1][i])
            res.append(tmp_list)
        return res

so = Solution()
res = so.generate(5)
print res
