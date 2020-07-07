#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-07 11:54:41

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for tmp in strs:
            sort_tmp = ''.join(sorted(tmp))
            if sort_tmp in res:
                res[sort_tmp].append(tmp)
            else:
                res[sort_tmp] = []
                res[sort_tmp].append(tmp)
        final_res = []
        for k, v in res.items():
            final_res.append(v)
        return final_res


s = Solution()
# val = ["eat", "tea", "tan", "ate", "nat", "bat"]
val = ["", ""]
res = s.groupAnagrams(val)
print res

