class Solution:
    def find_min(self, x, nums):
        for idx in range(len(nums)):
            if nums[idx] <= x:
                break
        if nums[idx] <= x:
            return idx - 1
        return idx

    def reverse(self, nums, start=0):
        nums_len = len(nums)
        for idx in range((nums_len-start)//2):
            t = nums[idx+start]
            nums[idx+start] = nums[nums_len - idx - 1]
            nums[nums_len - idx - 1] = t
        return nums

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a_idx = None
        b_idx = None
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] < nums[idx+1]:
                target = self.find_min(nums[idx], nums[idx+1:])
                a_idx = idx
                b_idx = idx + target + 1
                break
        if a_idx is not None:
            t = nums[a_idx]
            nums[a_idx] = nums[b_idx]
            nums[b_idx] = t
            self.reverse(nums, a_idx + 1)
        else:
            self.reverse(nums)
        print(nums)
s = Solution()
#a = [1,2,3]
#a = [2,3,1]
a = [5,4,7,5,3,2]
s.nextPermutation(a)
