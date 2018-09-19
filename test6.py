class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pos_list = range(numRows)
        row = 0
        column_p = 0
        res = []
        line = []
        p = 0
        while True:
            if p > len(s)-1:
                break
            if numRows == 1:
                line = [s[p]]
                p += 1
            elif row % (numRows - 1) == 0:
                line = [None] * numRows
                for idx, x in enumerate(s[p: p + numRows]):
                    line[idx] = x
                p = p + numRows
            else:
                line = [None] * numRows
                line[ numRows - 1 - row % (numRows - 1)] = s[p]
                p += 1
            res.append(line)
            row += 1
        print(res)
        out = []
        for column in range(numRows):
            for row in res:
                if row[column]:
                    out.append(row[column])
        return ''.join(out)


a = "PAYPALISHIRING"
print(a)
s = Solution()
print(s.convert(a, 4))

