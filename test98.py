#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 23:19:41

# Definition for a binary tree node.
from collections import deque



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Tree(object):
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret

class Solution(object):

    def process(self, root):
        if root is None:
            return True, None, None

        tmp_res, left_min, left_max  = self.process(root.left)
        if tmp_res is False or (left_max is not None and left_max >= root.val):
            return False, None, None

        tmp_res, right_min, right_max  = self.process(root.right)
        if tmp_res is False or (right_min is not None and right_min <= root.val):
            return False, None, None

        min_val = left_min if left_min else root.val
        max_val = right_max if right_max else root.val

        return True, min_val, max_val

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.process(root)
        return res[0]


so = Solution()
# a = TreeNode(10)
# a.left = TreeNode(9)
# a.right = TreeNode(101)
# a = None
a = Tree()
# in_list = [5,1,4,None,None,3,6]
# in_list = [3,None,30,10,None,None,15,None,45]
in_list = [3,None,30,10,None,None,15,None,45]
a.construct_tree(in_list)
res = so.isValidBST(a.root)
print res
