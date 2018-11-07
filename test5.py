class Solution(object):
    def gen_p1(self, idx, s):
        tmp_max = s[idx]
        move = 1
        while True:
            if idx - move >= 0 and idx + move < len(s) and s[idx-move] == s[idx+move]:
                tmp_max = s[idx-move] + tmp_max + s[idx+move]
                move += 1
            else:
                return tmp_max

    def gen_p2(self, idx, s):
        if s[idx] == s[idx + 1]:
            tmp_max = s[idx] + s[idx + 1]
        else:
            return ''

        move = 1
        while True:
            if idx - move >= 0 and idx + move + 1 < len(s) and s[idx-move] == s[idx+move+1]:
                tmp_max = s[idx-move] + tmp_max + s[idx+move+1]
                move += 1
            else:
                return tmp_max




    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        max_s = ''
        for idx, letter in enumerate(s):
            tmp_max = self.gen_p1(idx, s)
            if len(tmp_max) >= len(max_s):
                max_s = tmp_max

            if idx == len(s) - 1:
                continue

            tmp_max = self.gen_p2(idx, s)
            if len(tmp_max) >= len(max_s):
                max_s = tmp_max

        return max_s


s = Solution()
a = "arra"
res = s.longestPalindrome(a)
print(res)
