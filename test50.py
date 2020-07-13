#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-07 15:24:48


class Solution(object):



    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            flag = -1
            n = -n
        else:
            flag = 1

        def process(x, n):
            if n > 1:
                half_tmp = process(x, n / 2)
                if n % 2 == 1:
                    return half_tmp * half_tmp * x
                else:
                    return half_tmp * half_tmp
            elif n == 1:
                return x
            else:
                return 1
        tmp = process(x, n)
        if flag == -1:
            return 1/tmp
        else:
            return tmp




so = Solution()
res = so.myPow(2.00000, 10)
print res

res = so.myPow(2.10000, 3)
print res

res = so.myPow(2.00000, -2)
print res

res = so.myPow(0.44528, 0)
print res

