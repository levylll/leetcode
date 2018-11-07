class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums[:-1]):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]





nums = [-3,4,3,90]
0
target = 0

a = Solution()
print a.twoSum(nums, target)
