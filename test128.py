#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-06-08 10:45:02

from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_dict = defaultdict(int)
        for num in nums:
            # print '---------------------'
            # print num, tmp_dict
            if num in tmp_dict:
                continue

            max_len = 0
            tmp = num-1
            if tmp in tmp_dict:
                # print 'l', tmp_dict[tmp]
                max_len += tmp_dict[tmp]

            tmp = num+1
            if tmp in tmp_dict:
                # print 'r', tmp_dict[tmp]
                max_len += tmp_dict[tmp]

            tmp_dict[num] = max_len + 1
            # print max_len
            i = 1
            while num-i in tmp_dict:
                tmp_dict[num-i] = tmp_dict[num]
                i += 1

            i = 1
            while num+i in tmp_dict:
                tmp_dict[num+i] = tmp_dict[num]
                i += 1


        # print tmp_dict
        return max(tmp_dict.values())

so = Solution()
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [0,3,7,2, 5, 8, 4, 6, 1]
# print len(nums)
res =so.longestConsecutive(nums)

print res
