class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        pre_x = None
        for x in range(len(nums) - 3):
            if nums[x] == pre_x:
                continue
            pre_x = nums[x]
            pre_y = None
            for y in range(x+1, len(nums) - 2):
                if nums[y] == pre_y:
                    continue
                pre_y = nums[y]
                need = target - (nums[x] + nums[y])
                start = y + 1
                end = len(nums) - 1
                pre_start = None
                pre_end = None
                move = False
                while start < end:
                    if move:
                        if nums[start] == pre_start and nums[end] == pre_end:
                            start += 1
                            end -= 1
                            continue
                    move = False
                    pre_start = nums[start]
                    pre_end = nums[end]

                    if nums[start] + nums[end] == need:
                        tmp = [nums[x], nums[y], nums[start], nums[end]]
                        res.append([nums[x], nums[y], nums[start], nums[end]])
                        move = True
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] > need:
                        end -= 1
                    else:
                        start += 1

        return res


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
