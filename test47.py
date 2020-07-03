#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-04-25 17:54:34

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        out_list = []
        bak = set()
        for idx, head in enumerate(nums):
            if head in bak:
                continue
            bak.add(head)
            for tmp in self.permuteUnique([x for tmp_idx, x in enumerate(nums) if tmp_idx != idx]):
                out_list.append([head] + tmp)
        return out_list

    '''
    def add_tail(self, nums):
        if nums:
            return [head] + self.add_tail([x for x in nums if x != head])
        else:
            return [head]
    '''


s = Solution()
# a = [1,2,3]
# a = [1, 2, 1]
a = [1, 1, 2]

print s.permuteUnique(a)
