class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        flag = None
        res = ''
        s = s.strip()
        if not s:
            return 0
        elif s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            flag = 1
            s = s[1:]
        elif s[0] <= "9" and s[0] >= "0":
            flag = 1
        else:
            return 0
        s = s.strip()
        if not s:
            return 0
        elif s[0] == '+':
            return '+'
        other = ""
        for idx, x in enumerate(s):
            if x <= "9" and x >= "0":
                res += str(x)
            else:
                other = x
                break
        if not res:
            return other
        if (flag == 1 and int(res) > 2**31 - 1):
            return 2**31 - 1
        elif (flag == -1 and int(res) > 2 ** 31):
            return - 2 ** 31
        else:
            return flag * int(res)

s = Solution()
print(s.myAtoi("+234"))
