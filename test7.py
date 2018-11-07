class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        s = str(x)
        start = 0
        res = ''
        for num in range(len(s)):
            if start == 0 and s[-1 - num] == 0:
                    continue
            res += s[-1 - num]
            start = 1
        if flag == -1:
            if int(res) > 2 ** 31:
                return 0
            else:
                return -int(res)
        else:
            if int(res) > 2 ** 31 -1
                return 0
            else:
                return int(res)

s = Solution()
print(s.reverse(123))


