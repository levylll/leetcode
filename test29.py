class Solution:
    def accumulation(self, dividend, divisor):
        cnt = 0
        total = 0
        while total < dividend:
            total += divisor * (2 ** cnt)
            cnt += 1

        return cnt

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        tmp = 2**31
        positive = True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor

        #if dividend < -tmp or dividend > tmp-1:
            #return tmp-1

        cnt = self.accumulation(dividend, divisor)
        total = 0
        res = 0
        for x in range(cnt, -1, -1):
            tmp = 2 ** x
            if total + divisor * tmp <= dividend:
                total += divisor * tmp
                res += 2 ** x

        res =  res if positive else -res
        return 2**31 -1 if res < - 2 ** 31 or res > 2 ** 31 - 1 else res

s = Solution()
print(s.divide(-2147483648, -1))
#print(s.divide(2147483647, 1))
