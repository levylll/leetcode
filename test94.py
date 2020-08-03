#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 15:59:55


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def process(self, res, root):
        if root:
            tmp = self.process(res, root.left)
            if tmp:
                res.append(tmp.val)

            res.append(root.val)
            tmp = self.process(res, root.right)
            if tmp:
                res.append(tmp.val)
        return None

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.process(res, root)
        return res



so = Solution()
root = TreeNode(19)
root.left = TreeNode(10)
root.right = TreeNode(11)
res = so.inorderTraversal(root)
print res
