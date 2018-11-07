class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while l < r:
            if l + 1 == r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[-1] > nums[mid]:
                # 右侧递增
                if target <= nums[r] and target > nums[mid]:
                    l = mid
                else:
                    r = mid
            else:
                # 左侧递增
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid
        return -1




# nums = [4,5,6,7,0,1,2]
# target = 7
# nums = [4,5,6,7,0,1,2]
# target = 0
# nums = [3, 1]
# target = 0
nums = [1,3,5]
target = 5
# nums = [1]
# target = 1
s = Solution()
print(s.search(nums, target))
