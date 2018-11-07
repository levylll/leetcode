class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        nn = len(nums)
        while idx < nn:
            if val == nums[idx]:
                del nums[idx]
                nn -= 1
            else:
                idx += 1
        return idx
