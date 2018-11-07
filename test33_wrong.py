class Solution:
    def bisearch(self, nums, target):
        mid = len(nums) // 2
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        if len(nums) == 0:
            return -1
        if target < nums[mid]:
            res = self.bisearch(nums[:mid], target)
            if res != -1:
                return res
            return -1
        elif target > nums[mid]:
            res = self.bisearch(nums[mid+1:], target)
            if res != -1:
                return mid+res
            return -1
        else:
            return mid

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 0:
            return -1
        mid = len(nums) // 2
        if nums[-1] >= nums[mid]:
            if target <= nums[-1] and target >= nums[mid]:
                res = self.bisearch(nums[mid:], target)
                print(res)
                if res != -1:
                    return res + mid
                return -1
            else:
                res = self.search(nums[:mid], target)
                if res != -1:
                    return res
                return -1
        elif nums[-1] <= nums[mid]:
            if target <= nums[mid] and target >= nums[0]:
                res = self.bisearch(nums[:mid+1], target)
                if res != -1:
                    return res
                return -1
            else:
                res = self.search(nums[mid+1:], target)
                if res != -1:
                    return res + mid
                return -1


# nums = [4,5,6,7,0,1,2]
# target = 7
# nums = [3, 1]
# target = 1
nums = [1,3]
target = 3
s = Solution()
print(s.search(nums, target))
