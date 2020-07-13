#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-10 16:39:23

class Solution(object):
    def p_merge(self, a, b):
        # print a[0], b[0],  a[1], b[1]
        # print a[0] <= b[0] and a[1] >= b[1]
        if (b[0] <= a[0] and b[1] >= a[0]) or (a[0] <= b[0] and a[1] >= b[0]):
            return [min((a[0], b[0])), max((a[1], b[1]))]
        return None

    def process(self, intervals):
        if len(intervals) <= 1:
            return intervals[0], None

        res = []
        src = intervals[0]
        for i in range(1, len(intervals)):
            tmp = self.p_merge(src, intervals[i])
            if tmp:
                intervals[i] = tmp
                return None, intervals[1:]
        return src, intervals[1:]

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        res = []
        for _ in range(len(intervals)):
            head, intervals = self.process(intervals)
            # print head, intervals
            if head:
                res.append(head)
        return res

so = Solution()
a = [[1,3],[2,6],[8,10],[15,18]]
res = so.merge(a)
print res

a = [[1,4],[4,5]]
res = so.merge(a)
print res
