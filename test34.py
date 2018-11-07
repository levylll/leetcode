#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2019-07-24 17:15:51


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        target_index = self.search_target(0, len(nums)-1, nums, target)
        if target_index == '-1':
            return [-1, -1]

        # print target_index
        left = target_index
        right = target_index
        while left > 0:
            if nums[left-1] == target:
                left-=1
                continue
            break

        while right < len(nums)-1:
            if nums[right+1] == target:
                right+=1
                continue
            break

        return [left, right]

    def search_target(self, left, right, nums, target):
        mid = (left+right)/2
        # print left, right, mid
        if left == mid:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1


        if nums[mid] > target:
            return self.search_target(left, mid, nums, target)
        elif nums[mid] < target:
            return self.search_target(mid, right, nums, target)
        else:
            return mid

s = Solution()
# print s.searchRange([1, 4], 4)
print s.searchRange([1,2,3,3,3,3,4,5,9], 3)
