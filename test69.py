#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-14 14:07:33

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ori = x
        start = 0
        end = x
        # if x == 1:
        #     return 1

        while True:
            tmp = int((start+end)/2)
            print start, end, tmp
            # exit()
            if tmp * tmp <= x:
                if (tmp+1) * (tmp+1) > x:
                    return tmp
                else:
                    start = tmp
            else:
                end = tmp


sol = Solution()
res = sol.mySqrt(1)
print res
