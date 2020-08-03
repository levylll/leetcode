#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 12:09:59

class Solution(object):

    def numDecodings(self, s):

        if len(s) == 0:
            return 0
        elif len(s) == 1 and s[0] != '0':
            return 1
        elif s[0] == '0':
            return 0

        res = [0] * (len(s) + 1)
        res[0] = 1

        if s[1] == '0':
            if int(s[0:2]) > 26:
                return 0
            else:
                res[1] = 1
        else:
            if int(s[0:2]) <= 26:
                res[1] = 2
            else:
                res[1] = 1

        for x in range(2, len(s)):
            if s[x-1] == '0':
                if s[x] == '0':
                    return 0
                else:
                    res[x] = res[x-1]
            else:
                if int(s[x-1:x+1]) > 26:
                    if s[x] == '0':
                        return 0
                    else:
                        res[x] = res[x-1]
                else:
                    if s[x] == '0':
                        res[x] = res[x-2]
                    else:
                        res[x] = res[x-2] + res[x-1]
        return res[-2]



# a = '226'
a = '0'
a = '10'
# a = '01'
# a = '100'
a = '230'
a = '220'
# a = '12'
a = '1'
a = '10'
a = '26'
so = Solution()
res = so.numDecodings(a)
print res
