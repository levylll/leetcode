class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = strs[0]
        for s in strs[1:]:
            tmp = ""
            for pair in zip(res, s):
                if pair[0] == pair[1]:
                    tmp += pair[0]
                else:
                    break
            res = tmp
        return res


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
