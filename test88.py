#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 11:24:50

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        nums1[:] = nums1[:m]
        nums2 = nums2[:n]
        while p2 < len(nums2) and p1 < len(nums1):
            if nums2[p2] < nums1[p1]:
                nums1.insert(p1, nums2[p2])
                # nums1[p1+1:] = nums1[p1:]
                # nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        if p2 < len(nums2):
            nums1.extend(nums2[p2:])


if __name__ == '__main__':
    so = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    so.merge(nums1, m, nums2, n)
    print nums1


