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

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        flag = True
        level = [root]
        while level:
            tmp_level = []
            tmp_res = []
            for elem in level:
                if elem:
                    tmp_res.append(elem.val)
                    tmp_level.append(elem.left)
                    tmp_level.append(elem.right)

            if tmp_res:
                if flag is False:
                    res.append(tmp_res[::-1])
                    flag = True
                else:
                    res.append(tmp_res)
                    flag = False

            level = tmp_level
        return res





so = Solution()
# a = TreeNode(10)
# a.left = TreeNode(9)
# a.right = TreeNode(101)
# a = None
a = Tree()
# in_list = [5,1,4,None,None,3,6]
# in_list = [3,None,30,10,None,None,15,None,45]
# in_list = [3,None,30,10,None,None,15,None,45]
in_list = [3,9,20,None,None,15,7]
a.construct_tree(in_list)
res = so.zigzagLevelOrder(a.root)
print res
