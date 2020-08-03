#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 12:09:59

class Solution(object):

    def trans(self, a):
        if a and int(a) != 0:
            return '%c' %(int(a) - 1 + ord('A'))
        return None

    def numDecodings(self, s):

        res = self.process(s)
        if res:
            return len(res)
        return 0

    def process(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0 and s[0] == '0':
            return None

        if len(s) == 1:
            if s[0] != 0:
                tmp_res = self.trans(s[0])
                if tmp_res:
                    return [tmp_res]
                else:
                    return None
            else:
                return None
        elif len(s) == 0:
            return []

        res = []

        # 1位数字
        tmp = s[0]
        if tmp != 0:
            tmp = self.trans(tmp)
            tmp_list = self.process(s[1:])
            if tmp_list is not None:
                if tmp_list:
                    for elem in tmp_list:
                        res.append('%s%s'%(tmp, elem))
                else:
                    res.append('%s'%(tmp))

        # 2位数字
        tmp = int(s[0:2])
        if tmp <= 26 and tmp > 0:

            tmp = self.trans(tmp)
            tmp_list = self.process(s[2:])
            if tmp_list is not None:
                if tmp_list:
                    for elem in tmp_list:
                        res.append('%s%s'%(tmp, elem))
                else:
                    res.append('%s'%(tmp))
        if res:
            return res
        else:
            return None


a = '226'
a = '0'
a = '10'
a = '01'
a = '100'
a = '230'
so = Solution()
res = so.numDecodings(a)
print res
