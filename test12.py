class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rows = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        codebook = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        idx = 0
        s = ''
        while num > 0:
            cnt = 0
            if num >= rows[idx]:
                cnt = num // rows[idx]
            s += codebook[idx] * cnt
            num -= cnt * rows[idx]
            idx += 1

        return s


s = Solution()
print(s.intToRoman(1))



