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

        max_reach = nums[0]
        now_reach = 0
        step = 0
        for i in range(len(nums)):
            if nums[i] + i > max_reach:
                max_reach = nums[i] + i

            # print i, nums[i], max_reach
            if nums[i] + i >= len(nums) - 1:
                return step + 1

            if i == now_reach:
                step += 1
                now_reach = max_reach

        return step


            # maxnums[x]


so = Solution()
# a = [2,3,1,1,4]
a = [2,3,0,1,4]
# a = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
# a = [1]
# a = [10,9,8,7,6,5,4,3,2,1,1,0]
print so.jump(a)
