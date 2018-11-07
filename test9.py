class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        for idx in range(int(len(s)/2)):
            if s[idx] != s[-idx-1]:
                return False
        return True


s = Solution()
print(s.isPalindrome(-121))
