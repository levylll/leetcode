#!/usr/bin/env python
# -*- coding:utf8 -*-
# Power by levy@2020-07-01 17:12:15

class Solution(object):

    def process(self, candidates, target, start_i, tmp, ans, record):
        while start_i < len(candidates):
            tmp.append(candidates[start_i])
            if sum(tmp) == target:
                tmp_str = tuple(tmp)
                if tmp_str in record:
                    return
                record.append(tmp_str)
                ans.append([x for x in tmp])
                return

            if sum(tmp) > target:
                return
            self.process(candidates, target, start_i+1, [x for x in tmp], ans, record)
            start_i += 1
            tmp.pop(-1)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start_i = 0
        tmp = []
        ans = []
        record = []
        self.process(sorted(candidates), target, start_i, tmp, ans, record)
        return ans


s = Solution()
# candidates = [2, 3, 6, 7]
# target = 7
# candidates = [2, 3, 5]
candidates = [8, 7, 4, 3]
target = 11
res = s.combinationSum2(candidates, target)
print res
