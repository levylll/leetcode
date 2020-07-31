#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-14 17:10:51

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        tmp = nums[0]
        tmp_list = self.subsets(nums[1:])
        # print tmp, tmp_list
        res = []
        # print tmp_list
        if tmp_list:
            print tmp_list
            for elem in tmp_list:
                res.append([tmp]+elem)
                res.append(elem)
        else:
            res = [[tmp], []]
        return res

so = Solution()
nums = [1,2,3]
res = so.subsets(nums)
print res

