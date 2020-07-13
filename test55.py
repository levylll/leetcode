#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-10 12:06:05

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums) - 1
        for i in range(nums_len)[::-1]:
            if nums[i] >= (nums_len-i):
                nums_len = i
        if nums_len == 0:
            return True
        return False


so = Solution()
a = [2,3,1,1,4]
res = so.canJump(a)
print res

a = [3,2,1,0,4]
res = so.canJump(a)
print res
