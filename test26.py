class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_l = len(nums)
        x = 0
        pre = None
        cnt = 0
        while x < max_l:
            if nums[x] == pre:
                nums.pop(x)
                max_l-= 1
            else:
                pre = nums[x]
                x += 1
        return x

s = Solution()
nums = [1,1,3]
print(s.removeDuplicates(nums))




