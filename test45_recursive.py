#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-05-17 09:13:06

class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # print nums

        if len(nums) == 1:
            return 0

        if nums[0] == 0:
            return -1

        if nums[0] >= len(nums) - 1:
            return 1

        res = []
        for x in range(nums[0]):

            tmp = self.jump(nums[x+1:])

            if tmp == -1:
                continue

            res.append(tmp)

        if len(res):
            return 1 + min(res)

        return -1


so = Solution()
# a = [2,3,1,1,4]
# a = [2,3,0,1,4]
a = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
print so.jump(a)
