#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-03 16:39:52

class Solution(object):
    def cal(self, height, need_equal=True):
        start_x = 0
        res = [0]
        for x in height:
            if x != 0:
                if start_x == 0:
                    res.append(0)
                    start_x = x
                else:
                    # print x, start_x
                    if x < start_x:
                        res[-1] += (start_x - x)
                    elif x == start_x and not need_equal:
                        continue
                    else:
                        res.append(0)
                        start_x = x
            else:
                if start_x != 0:
                    res[-1] += start_x

        res.pop(-1)
        if res:
            return sum(res)
        else:
            return 0

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res1 = self.cal(height, True)
        res2 = self.cal(height[::-1], False)
        print res1, res2
        return res1 + res2

s = Solution()



a = [0,1,0,2,1,0,1,3,2,1,2,1]
res = s.trap(a)
print res


a = [2, 0, 2]
res = s.trap(a)
print res
