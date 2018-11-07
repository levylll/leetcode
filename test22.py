class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 1:
            return ['()']
        else:
            for elem in self.generateParenthesis(n-1):
                for x in range(len(elem) + 1):
                    res.append('(' + elem[:x] + ')' + elem[x:])

        return list(set(res))

s = Solution()
print(s.generateParenthesis(3))

