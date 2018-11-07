class Solution:

    def max_valid(self, s):
        if len(s) > 2:
            valid1, max_len1 = self.max_valid(s[1:-1])
            valid2, max_len2 = self.max_valid(s[2:])
            valid3, max_len3 = self.max_valid(s[:-2])
            if valid1 and s[0] == '(' and s[-1] == ')':
                return True, 2 + max_len1
            elif valid2 and s[0] == '(' and s[1] == ')':
                return True, 2 + max_len2
            elif valid3 and s[-2] == '(' and s[-1] == ')':
                return True, 2 + max_len3
            else:
                _, max_len4 = self.max_valid(s[1:])
                _, max_len5 = self.max_valid(s[:-1])
                # print('======')
                # print(s[1:], max_len2)
                # print(s[:-1], max_len3)
                return False, max(max_len1, max_len2, max_len3, max_len4, max_len5)
        elif len(s) == 2:
            if s[0] == '(' and s[-1] == ')':
                return True, 2
            else:
                return False, 0
        elif len(s) == 1:
            return False, 0
        else:
            return True, 0

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid, max_len = self.max_valid(s)
        return max_len

s = Solution()
#a = "(()"
#a = ")()())"
#a = "((()))())"
#a = ")(((((()())()()))()(()))("
print(s.longestValidParentheses(a))
