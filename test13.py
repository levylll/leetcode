class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        info = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        s_str = str(s)
        #s_str = s_str[::-1]
        res = 0
        while len(s_str):
            if s_str[:2] in info:
                res += info[s_str[:2]]
                s_str = s_str[2:]
            else:
                res += info[s_str[0]]
                s_str = s_str[1:]
        return res

s = Solution()
print(s.romanToInt("MCMXCIV"))
