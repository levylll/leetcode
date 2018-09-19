import fire

from math import fabs

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x_list = set()
        min_res = None
        nums = sorted(nums)
        print(nums)
        for x in range(len(nums) - 2):
            if nums[x] in x_list:
                continue
            x_list.add(nums[x])
            y = x + 1
            z = len(nums) - 1
            #if nums[x] != -1:
                #continue
            while y < z:
                real = nums[x] + nums[y] + nums[z] - target
                tmp = fabs(real)
                if min_res  == None or min_res > tmp:
                    min_res = tmp
                    res = nums[x] + nums[y] + nums[z]
                if real > 0:
                    z -= 1
                elif real < 0:
                    y += 1
                else:
                    return res
        return res


s = Solution()
print(s.threeSumClosest([0, 2, 1, -3], 1))
