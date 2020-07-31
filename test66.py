#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-13 16:41:06


class Solution(object):
    def process(self, digits, pos):
        if pos == -1:
            digits.insert(0, 1)
        else:
            if digits[pos] == 9:
                digits[pos] = 0
                self.process(digits, pos - 1)
            else:
                digits[pos] += 1


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.process(digits, len(digits)-1)
        return digits


sol = Solution()
a = [1,2,9]
res = sol.plusOne(a)
print res

a = [9]
res = sol.plusOne(a)
print res
