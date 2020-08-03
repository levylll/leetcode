#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 22:59:40

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def check_syn(self, root_list):
        for i in range(len(root_list)/2):
            if root_list[i] and root_list[len(root_list) - i - 1] and root_list[i].val == root_list[len(root_list) - i - 1].val:
                continue
            elif root_list[i] is None and root_list[len(root_list) - i - 1] is None:
                continue
            else:
                return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level = [root]
        while level:
            if self.check_syn(level):
                tmp_list = []
                for elem in level:
                    if elem:
                        tmp_list.append(elem.left)
                        tmp_list.append(elem.right)
                level = tmp_list
            else:
                return False
        return True

so = Solution()
a = TreeNode(10)
a.left = TreeNode(10)
# a.right = TreeNode(10)
res = so.isSymmetric(a)

print res
