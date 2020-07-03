#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-03 11:26:42

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        miss_n = set([1])
        for x in nums:
            if x <= 0:
                continue
            if x in miss_n:
                miss_n.remove(x)

            tmp_miss = x + 1
            if tmp_miss in nums:
                continue
            if tmp_miss not in miss_n:
                miss_n.add(tmp_miss)
        return min(miss_n)

s = Solution()

input = [7,8,9,11,12]
res = s.firstMissingPositive(input)
print res

input = [2, 1]
res = s.firstMissingPositive(input)
print res

