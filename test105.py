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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        print preorder, inorder

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        root.left = self.buildTree(preorder[1: i+1], inorder[0: i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root




so = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
res = so.buildTree(preorder, inorder)
print res
