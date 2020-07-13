#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-07 17:10:53

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records = []
        for i in range(len(nums)):
            if i == 0:
                records.append(nums[i])
            else:
                pre = max(0, records[i-1])
                now = pre + nums[i]
                records.append(now)
        return max(records)

so = Solution()
res = so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print res
