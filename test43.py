#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-05-12 17:29:09

class Solution(object):

    def fun_mult(self, num1_list, val, pos, res):
        if val == 0:
            return res

        for i in range(len(num1_list)):
            # print res, num1_list
            res[i+pos] += num1_list[-i-1] * val
        return res

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            tmp = num2
            num2 = num1
            num1 = tmp


        if num1 == '0' or num2 == '0':
            return '0'

        res = [0] * (len(num1) + len(num2) + 1)
        num1_list = [int(x) for x in num1]
        num2_list = [int(x) for x in num2]
        for i in range(len(num2)):
            res = self.fun_mult(num1_list, num2_list[-i-1], i, res)

        flag = 0
        for i in range(len(res)-1):
            tmp = int(res[i] / 10)
            res[i] = res[i] % 10
            res[i+1] += tmp

        final_res = []
        start = True
        for i in range(len(res)):
            if start and res[-i-1] == 0:
                continue
            start=False
            final_res.append(res[-i-1])
        return ''.join(map(str, final_res))

sol = Solution()
# print sol.multiply('21', '51')
# print sol.multiply('6', '501')
print sol.multiply('52', '60')

