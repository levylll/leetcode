class Solution(object):
    def gen_min_num(self, num):
        if len(num) >= 1:
            if num[0] < num[-1]:
                return 0
            else:
                return -1
        else:
            return None

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenth = len(nums1) + len(nums2)
        need_idx = lenth/2
        first = 0
        second = 0
        idx = 0
        while idx <= need_idx:
            first=second
            if not nums1:
                second = nums2.pop(self.gen_min_num(nums2))
                idx += 1
                continue
            elif not nums2:
                second = nums1.pop(self.gen_min_num(nums1))
                idx += 1
                continue

            if nums1[self.gen_min_num(nums1)] < nums2[self.gen_min_num(nums2)]:
                second = nums1.pop(self.gen_min_num(nums1))
            else:
                second = nums2.pop(self.gen_min_num(nums2))
            idx += 1

        if lenth%2 == 0:
            res = (first + second)/2
        else:
            res = second
        return res

s = Solution()
res = s.findMedianSortedArrays([1, 2], [3, 4])
print(res)
