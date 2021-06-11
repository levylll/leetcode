#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-06-08 10:23:21

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_res1 = 0 if 0 in nums else nums[0]
        a = 1
        for i in nums:
            if i == 0:
                a = 1
                continue

            a = a*i
            if a > max_res1:
                max_res1 = a

        a = 1
        for i in nums[::-1]:
            if i == 0:
                a = 1
                continue

            a = a*i
            if a > max_res1:
                max_res1 = a
        return max_res1


so = Solution()
nums = [2,-3,-2,4]
print so.maxProduct(nums)

