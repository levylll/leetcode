class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if "*" not in p and "." not in p and s != p:
            return False

        #print('%s:%s' %(s, p))
        if not s and not p:
            return True
        elif not s:
            if p[-1] == '*':
                return self.isMatch(s, p[:-2])
            else:
                return False
        elif not p:
            return False


        if p[-1] == ".":
            return self.isMatch(s[:-1], p[:-1])
        elif p[-1] == "*":
            if p[-2] == '.' or s[-1] == p[-2]:
                return self.isMatch(s[:-1], p) or self.isMatch(s[:], p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        elif p[-1] == s[-1]:
            return self.isMatch(s[:-1], p[:-1])
        else:
            return False


s = Solution()
print(s.isMatch("aasdfasdfasdfasdfas","aasdf.*asdf.*asdf.*asdf.*s"))
