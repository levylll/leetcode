class Solution:
    def __init__(self):
        self.num_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["h", "i", "j"],
            "5": ["k", "l", "m"],
            "6": ["n", "o", "p"],
            "7": ["q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
    def func(self, digits):
        res = []
        if len(digits) > 1:
            for x in self.num_dict[digits[0]]:
                #print(len(digits))
                #print(x)
                for y in self.func(digits[1:]):
                    res.append(x+y)
            return res
        elif digits:
            return self.num_dict[digits[0]]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            return self.func(str(digits))
        else:
            return []

s = Solution()
print(s.letterCombinations("23"))
