#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-31 14:49:40

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        i = 0
        opt = 0
        while i < total and opt < total:
            print nums, i
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
            else:
                i += 1
            opt += 1
        return nums


so = Solution()
a = [2,0,2,1,1,0]
res = so.sortColors(a)
print res


